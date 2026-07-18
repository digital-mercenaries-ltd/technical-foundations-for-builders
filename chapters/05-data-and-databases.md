# Chapter 5: Data and databases

Software becomes responsible for data when it gives facts a representation, accepts changes and later makes decisions from what was stored. A database is not merely a place to put objects. Its model, rules and guarantees determine which questions are easy to answer, which mistakes it can reject and what simultaneous users can observe.

This chapter assumes only the computing, programming, engineering and web ideas introduced in [Chapters 1–4](../README.md#map-of-the-territory). The entries reuse a small order system—customers, orders, products and order items—so that each new mechanism extends one familiar example. Every entry also defines enough locally to be read on its own.

The focus is structure, integrity and safe change inside a data store. Replication and distributed coordination belong in Chapter 6, responsibility for managed databases in Chapter 7, backups and recovery evidence in Chapter 8, database security in Chapter 9, and legal retention or erasure obligations in Chapter 11.

## Chapter map

The first pass covers:

1. [Data models, schemas, identifiers and missing values](#data-models-schemas-identifiers-and-missing-values)
2. [Relational databases, Structured Query Language, keys, relationships and joins](#relational-databases-structured-query-language-keys-relationships-and-joins)
3. [Constraints, validation and data integrity](#constraints-validation-and-data-integrity)
4. [Queries, indexes and execution plans](#queries-indexes-and-execution-plans)
5. [Transactions, atomicity, isolation and concurrency control](#transactions-atomicity-isolation-and-concurrency-control)
6. [Schema evolution, online migrations and backfills](#schema-evolution-online-migrations-and-backfills)
7. [Non-relational databases, consistency and the data lifecycle](#non-relational-databases-consistency-and-the-data-lifecycle)

## Data models, schemas, identifiers and missing values

*Stored data is a designed representation of reality, not reality itself.*

### What they are

A **data model** describes the things a system records, their properties, their relationships and the operations that make sense. An order system might represent customers, products, orders and order items. It must decide whether an order keeps the product's current description or a historical snapshot, and whether a cancelled order is changed, marked or removed. Those are product meanings before they are database details.

A **schema** makes selected parts of the model explicit: names, types, required values, relationships and rules. In a relational database, a table has named columns and a changing set of rows. A document store might permit different fields in different documents, but applications still depend on field names and meanings. “Schemaless” therefore means that less structure is enforced centrally, not that the data has no expected structure.

An **identifier** distinguishes one thing from another within a stated scope. `customer_123` might be a public customer identifier; a database key might identify the stored customer row; and an idempotency key might identify one attempted API operation. These identifiers can have different formats and jobs. A Universally Unique Identifier (UUID) can be generated without a central counter, but uniqueness does not make it secret, unguessable or proof that its holder is authorised.

Missing values also need domain meaning. In the following JSON object, `middleName` is present with the value `null`:

```json
{"customerId":"customer_123","middleName":null}
```

Omitting the field is structurally different. Either form might mean “not supplied”, “not applicable” or “not yet checked”. An empty string, zero or a convenient default carries yet another meaning. In SQL expressions, `NULL` has special unknown-value behaviour and is tested with `IS NULL`, but the application's reason for storing it still requires an explicit decision.

### Why a builder needs to know this

These choices appear in application types, API messages, database columns, analytics and migrations. If the representation loses a distinction the product needs, later code cannot reliably reconstruct it. A stable model also lets several writers and readers agree on what stored data means while their implementations evolve.

### Pitfalls

- **“The schema is the real world.”** It is a useful, incomplete model whose assumptions need maintenance.
- **“An identifier is a password.”** Knowing an identifier must not automatically grant authority.
- **“Every row already has an identity.”** SQL does not create a useful row identifier unless the design declares one.
- **“A default fixes missing data.”** It can erase the distinction between a real value and missing knowledge.
- **“Rows come back in insertion order.”** A query must request an order when order matters.

### Related concepts in TFB

- [Values, types and conversions](02-programming-foundations.md#values-types-and-conversions) - declared application types do not transform or validate stored values by themselves.
- [Text, Unicode and character encodings](01-computing-foundations.md#text-unicode-and-character-encodings) - text identifiers cross interfaces with defined representations and comparison rules.
- [Functional requirements, specifications and invariants](03-software-engineering.md#functional-requirements-quality-attributes-specifications-and-invariants) - a data model records selected product requirements as structure and rules.

### Deeper concepts

- Domain modelling - discovering useful concepts, boundaries and language before choosing storage structures.
- Normalisation - separating relational facts to control duplication and update anomalies.
- Identifier design - choosing scope, stability, exposure and generation properties deliberately.

### Further reading

- [PostgreSQL: Table basics](https://www.postgresql.org/docs/current/ddl-basics.html) - a concise introduction to tables, columns, rows and ordering.
- [RFC 9562: Universally Unique IDentifiers](https://www.rfc-editor.org/rfc/rfc9562.html) - UUID formats, generation properties and security cautions.
- [JSON Schema: Object properties](https://json-schema.org/understanding-json-schema/reference/object) - examples of required, optional and `null` object members.
- [PostgreSQL: Comparison functions and operators](https://www.postgresql.org/docs/current/functions-comparison.html) - the special comparison behaviour of SQL null values.

## Relational databases, Structured Query Language, keys, relationships and joins

*A relational database stores facts in tables and lets queries combine them by declared relationships.*

### What they are

The **relational model** represents data as relations: sets of records with named attributes. A practical Structured Query Language (SQL) database exposes these as tables, rows and columns. SQL is largely **declarative**: a query says which result is required, while the database chooses physical steps for producing it. SQL products implement different dialects and extensions, so SQL and the mathematical relational model are related rather than interchangeable.

Suppose the order system has these tables:

```text
customers(customer_id, email)
orders(order_id, customer_id, placed_at)
order_items(order_id, product_id, quantity, unit_price)
products(product_id, current_name, stock)
```

A **key** is one or more columns used for identity or relationships inside this model. A **primary key** uniquely identifies a row and cannot be null. A **foreign key** records a reference to a key in another row, which may be in the same or another table, and can require the referenced row to exist. Here, `orders.customer_id` relates each order to its customer. The broader customer identifier discussed in the previous entry is a conceptual identity; a primary or foreign key is a database mechanism that may implement part of that identity policy.

A **join** combines rows that match a stated condition. An inner join between `orders` and `customers` can return orders with customer email addresses without copying the email into every order. A left join can retain every order and return null values where an optional matching row is absent. A foreign key does not fetch the customer automatically: the query still asks for the relationship it needs.

### Why a builder needs to know this

Relational databases are common foundations for transactional applications. Their model makes relationships and integrity rules visible while insulating callers from much of the physical storage. Understanding keys and joins helps you inspect generated schemas, recognise duplicated facts and question code that performs many small lookups instead of expressing the required result.

Object-relational mappers can translate objects and method calls into SQL. They reduce repetitive syntax but do not remove relational meaning, query cost, product differences or transaction behaviour. When an abstraction leaks, the underlying model remains the shortest route to a useful diagnosis.

### Pitfalls

- **“A table is a spreadsheet.”** It has database types, constraints and query semantics, not dependable visual position or row order.
- **“A foreign key loads related data.”** It can enforce a relationship; a query or mapper still selects what to retrieve.
- **“Joins are inherently slow.”** Cost depends on the requested result, data, access paths and chosen plan.
- **“An object-relational mapper replaces SQL knowledge.”** It generates database operations whose number and meaning still matter.
- **“SQL is identical everywhere.”** Types, null handling, features and syntax vary by product and version.

### Related concepts in TFB

- [Collections, data structures and algorithmic cost](02-programming-foundations.md#collections-data-structures-and-algorithmic-cost) - tables and indexes support operations with different costs.
- [Abstraction, information hiding and interfaces](03-software-engineering.md#abstraction-information-hiding-and-interfaces) - relational queries separate requested results from physical storage choices.
- [Client-server systems and behavioural contracts](04-internet-web-and-apis.md#client-server-systems-network-service-application-programming-interfaces-and-behavioural-contracts) - a database interface also includes behaviour beyond data shapes.

### Deeper concepts

- Relational algebra - the operations underlying relational queries.
- Normal forms - principles for locating facts and controlling harmful duplication.
- Object-relational mapping - translating between application objects and relational structures without hiding cost or guarantees.

### Further reading

- [E. F. Codd: A Relational Model of Data for Large Shared Data Banks](https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks) - the original argument for relations and data independence.
- [PostgreSQL: Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) - primary keys, foreign keys and other integrity mechanisms.
- [PostgreSQL: Table expressions](https://www.postgresql.org/docs/current/queries-table-expressions.html) - grounded examples of joins and their result sets.

## Constraints, validation and data integrity

*Friendly application checks and authoritative storage rules protect different paths into the same data.*

### What they are

**Data integrity** means that stored data continues to satisfy the rules needed for it to remain meaningful. A **database constraint** is a rule the database checks before accepting a state. Common relational constraints include declared types, `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY` and `CHECK` conditions.

The order system might define `order_items` with foreign keys to an order and product, plus these rules:

```sql
quantity   INTEGER NOT NULL CHECK (quantity > 0)
unit_price DECIMAL NOT NULL CHECK (unit_price >= 0)
```

The form or API can perform **application validation** and say “quantity must be at least 1” before doing more work. The database constraint separately rejects zero from any writer that reaches the same database: another application, an import, a background job or two requests whose actions overlap. Application validation knows request and user context and can give better feedback; a database constraint has wider authority over stored state. Neither universally replaces the other.

A constraint protects only the invariant it actually expresses and only within its scope. For example, a SQL check condition normally passes when its expression is true or unknown, so `CHECK (quantity > 0)` does not make quantity mandatory; `NOT NULL` states that separate rule. A database also cannot directly prove a current fact that exists only in a payment service or other remote system.

### Why a builder needs to know this

Validation code is easy to bypass accidentally as a system gains new write paths. Constraints make critical assumptions executable at the point shared by those writers. They turn some corrupting mistakes into explicit failures and make the schema a stronger record of intended state.

This is also an evidence boundary. Successful validation shows that one check accepted one input. Successful storage shows that the declared database rules accepted the resulting state. Neither proves that the business decision was correct or that every requirement was encoded.

### Pitfalls

- **“The browser already validated it.”** Client-side checks are useful feedback, not an authoritative storage boundary.
- **“The application is the only writer.”** Jobs, migrations, scripts and future services often prove otherwise.
- **“A constraint enforces what I meant.”** It enforces its precise expression, including product-specific null and comparison behaviour.
- **“Cascading deletion is convenient cleanup.”** It encodes an ownership rule and can remove far more data than intended.
- **“Valid data is authorised data.”** Input validity and permission are different concerns; authorisation belongs in Chapter 9.

### Related concepts in TFB

- [Functional requirements, specifications and invariants](03-software-engineering.md#functional-requirements-quality-attributes-specifications-and-invariants) - integrity rules are executable forms of selected invariants.
- [Testing, verification and evidence](03-software-engineering.md#testing-verification-and-evidence) - each validation layer supports a bounded correctness claim.
- [Values, types and conversions](02-programming-foundations.md#values-types-and-conversions) - parsing a value does not prove that the domain permits it.

### Deeper concepts

- Conditional and deferred constraints - enforcing rules whose timing or scope is more complex.
- Referential actions - deciding what happens to related rows when a referenced row changes or disappears.
- Cross-record invariants - rules that may require transactions, locking or a different model.

### Further reading

- [PostgreSQL: Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) - mechanics and qualifications for common relational constraints.
- [SQLite: Foreign key support](https://www.sqlite.org/foreignkeys.html) - an example of why constraint behaviour and configuration must be checked in the chosen product.
- [Ruby on Rails: Active Record validations](https://guides.rubyonrails.org/active_record_validations.html) - framework documentation that distinguishes application validation from database constraints.

## Queries, indexes and execution plans

*A useful question becomes work, and the database chooses how to perform that work.*

### What they are

A **query** requests data or a change. For a read query, a database **planner** considers possible operations and chooses an **execution plan**: a tree of scans, joins, sorts and other steps expected to produce the result at acceptable cost. The plan depends on the query, data distribution, statistics, available structures and database settings. Ten development rows are therefore weak evidence about behaviour with ten million production rows.

Without a suitable access path, the database may inspect every row. An **index** is an additional maintained structure that helps locate selected values or orderings, much as a book index points to pages without reproducing the book. Consider:

```sql
SELECT order_id, placed_at
FROM orders
WHERE customer_id = ?
ORDER BY placed_at DESC;
```

An index beginning with `customer_id` and then `placed_at` may help this access pattern. It consumes storage and must be updated when relevant rows change. The planner can still prefer a full scan when that is estimated to be cheaper, such as when most rows match.

Many databases expose plans through a command such as `EXPLAIN`. Estimates reveal what the planner expects; measured execution can reveal actual row counts and time. In PostgreSQL, `EXPLAIN ANALYZE` really executes the statement, including its side effects. A plan is diagnostic evidence, not a timeless property of the query.

One pattern worth recognising is **N+1 queries**: code loads 100 orders and then sends one customer query for each order, creating 101 database round trips. Each query may be fast in isolation while accumulated [latency](01-computing-foundations.md#latency-and-throughput) makes the request slow. The fix depends on the required result and should be measured, not guessed.

### Why a builder needs to know this

Database performance emerges from access patterns, data and maintained structures—not from query text alone. This model helps a builder ask for the slow query, its parameters, its plan, realistic data volume and observed timings before accepting “the database is slow” or “add an index” as an explanation.

### Pitfalls

- **“Indexes are free acceleration.”** They add storage, write work and maintenance.
- **“The database must use an index that exists.”** The planner chooses an estimated cheaper plan.
- **“Plan cost is milliseconds.”** Cost units are estimates for comparing candidate plans, not elapsed time.
- **“A fast query on sample data will stay fast.”** Distribution, volume, load and cache state can change the result.
- **“Measured explain is read-only.”** Some plan-inspection commands execute the statement; check before using them on changing queries.

### Related concepts in TFB

- [Collections, data structures and algorithmic cost](02-programming-foundations.md#collections-data-structures-and-algorithmic-cost) - indexes choose data structures for particular operations and growth patterns.
- [Latency and throughput](01-computing-foundations.md#latency-and-throughput) - query time and completed work require explicit boundaries and load.
- [Debugging and diagnosis](02-programming-foundations.md#debugging-and-diagnosis) - plans and timings replace performance guesses with causal evidence.

### Deeper concepts

- Selectivity and statistics - how the planner estimates the number of matching rows.
- Index structures and ordering - why different indexes suit different comparisons and sorts.
- Pagination and connection pools - controlling result size and concurrent access to database sessions.

### Further reading

- [PostgreSQL: Introduction to indexes](https://www.postgresql.org/docs/current/indexes-intro.html) - the basic lookup and maintenance trade-off.
- [PostgreSQL: Using `EXPLAIN`](https://www.postgresql.org/docs/current/using-explain.html) - reading plans, estimates and actual execution safely.
- [SQLite: Query planning](https://www.sqlite.org/queryplanner.html) - an accessible visual explanation from another database implementation.

## Transactions, atomicity, isolation and concurrency control

*Several valid steps do not automatically form one valid change when work overlaps or fails halfway.*

### What they are

A **transaction** groups database operations into one logical unit. **Atomicity** means its database effects commit together or roll back together. If creating an order requires an order row and three item rows, atomicity can prevent a failure from leaving only half of that database change.

**Atomicity, consistency, isolation and durability (ACID)** name four transaction properties. In this context, **consistency** means that a committed transaction preserves the rules defining a valid database state. It does not mean that every application decision was correct, nor does it describe which committed version a reader sees across replicated copies. That separate read or distributed-consistency question belongs with replication in Chapter 6. **Durability** means a committed result survives the failures covered by the database's stated guarantee, not every imaginable disaster.

**Concurrency** occurs when work overlaps. **Isolation** controls what concurrent transactions can observe and which combined outcomes can commit. Suppose two buyers each read `stock = 1`, subtract one locally and write `0`. Both orders may appear successful even though only one item existed. Starting transactions does not necessarily repair that unsafe read-modify-write sequence at every isolation level.

The invariant can instead be protected with a conditional atomic update, a lock, a version check or an isolation level strong enough for the whole operation. At **serializable** isolation, committed transactions must have an effect consistent with some one-at-a-time order. A database may abort one transaction to provide that guarantee, so the application must be prepared to retry the complete unit safely. Exact isolation levels and anomalies vary by product.

### Why a builder needs to know this

Reasoning that is sound for one request at a time can fail under ordinary simultaneous use. Builders need to identify the unit that must remain whole, the invariant that competing operations share and the database guarantee the code actually uses. A successful commit proves that the database accepted one transaction under those rules; it does not prove the business intent or an external payment result.

### Pitfalls

- **“Atomicity and isolation are the same guarantee.”** One groups effects; the other governs overlap.
- **“A transaction makes application logic correct.”** It protects only the operations and rules placed inside its boundary.
- **“The C in ACID means every reader sees the latest copy.”** ACID valid-state consistency and distributed read consistency are different concepts.
- **“A database transaction includes an email or payment API.”** External systems need coordination patterns covered in Chapter 6.
- **“The strongest isolation has no cost.”** Stronger guarantees can increase waiting, aborts or retry work.

### Related concepts in TFB

- [Variables, state, mutability and side effects](02-programming-foundations.md#variables-state-mutability-and-side-effects) - concurrent transactions are overlapping changes to shared state.
- [Errors, exceptions and cleanup](02-programming-foundations.md#errors-exceptions-and-cleanup) - every exit path must commit or roll back the transaction resource deliberately.
- [Testing, verification and evidence](03-software-engineering.md#testing-verification-and-evidence) - concurrency claims need tests and observations that actually exercise overlap.

### Deeper concepts

- Isolation anomalies and write skew - invalid outcomes permitted by particular isolation models.
- Optimistic and pessimistic concurrency control - detecting conflicts or preventing them with locks.
- Multi-system coordination - handling one business operation across a database and remote services.

### Further reading

- [PostgreSQL: Transactions tutorial](https://www.postgresql.org/docs/current/tutorial-transactions.html) - atomic commit and rollback through a worked account-transfer example.
- [PostgreSQL: Transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) - isolation levels, anomalies and retry requirements.
- [Microsoft: ACID properties](https://learn.microsoft.com/en-us/windows/win32/cossdk/acid-properties) - a compact account of the four properties and the application's remaining responsibility.

## Schema evolution, online migrations and backfills

*Changing stored structure is a compatibility operation across code, old data and live work.*

### What they are

A **database migration** changes a schema or stored representation. In a live service, old and new application versions can overlap while existing rows still reflect earlier expectations. A migration therefore changes a shared contract; it is not only a file that runs during deployment.

An **online migration** performs the change while acceptable service continues. “Online” does not mean instant, reversible, zero-cost or zero-risk. A statement that is harmless on an empty development database might lock a large production table, rewrite every row or compete with user traffic.

A common strategy is **expand, migrate, contract**:

1. Add a representation that old code can safely ignore.
2. Deploy code that tolerates both forms and writes the new one.
3. Migrate and verify existing data.
4. Switch readers after evidence shows the new representation is complete.
5. Remove the obsolete form only when nothing relies on it.

Suppose orders need a required `tax_amount`. Adding it as optional first lets current code continue. New code can calculate it for new orders. A **backfill** then populates old orders in bounded batches, records progress and reconciles results before a later constraint makes the field required. A backfill is production work over real volume, not merely a schema declaration; it must be restartable and avoid overwhelming normal traffic.

Temporary dual writes or dual reads can support the overlap, but they introduce another opportunity for values to disagree. Verification and reconciliation are part of the migration, not optional polish. A syntactically reversible migration also cannot recreate discarded meaning: code rollback does not recover a deleted column's unrecorded data.

### Why a builder needs to know this

Many database incidents arise from a correct destination design reached through an unsafe transition. Thinking in compatible stages lets builders question locks, load, mixed-version behaviour, failure recovery and evidence before a generated migration reaches production. It also connects schema evolution to the broader practice of [evolutionary replacement](03-software-engineering.md#refactoring-technical-debt-legacy-systems-and-evolutionary-replacement).

### Pitfalls

- **“The migration was fast locally.”** Local volume and concurrent load rarely represent production.
- **“Online means zero risk.”** Service can remain available while performance, lock and correctness risks still need control.
- **“Down migration means reversible.”** Destructive transformations can lose information that syntax cannot restore.
- **“Dual writing keeps itself consistent.”** Partial failure can leave old and new representations disagreeing.
- **“Deployment completion means backfill completion.”** Large data work can continue across many deployments and must expose progress.

### Related concepts in TFB

- [Version control, code review, shared ownership and recovery](03-software-engineering.md#version-control-code-review-shared-ownership-and-recovery) - source reversal and production-data reversal are different operations.
- [Build automation, continuous integration and fast feedback](03-software-engineering.md#build-automation-continuous-integration-and-fast-feedback) - automated deployment checks need compatibility assumptions, not merely successful syntax.
- [Client-server systems and behavioural contracts](04-internet-web-and-apis.md#client-server-systems-network-service-application-programming-interfaces-and-behavioural-contracts) - stored representations create compatibility commitments for their consumers.

### Deeper concepts

- Locking behaviour for schema changes - product-specific effects on concurrent reads and writes.
- Backfill orchestration and reconciliation - bounded, restartable processing with evidence of completeness.
- Change-data capture - observing committed changes while representations or systems coexist.

### Further reading

- [GitLab: Avoiding downtime in migrations](https://docs.gitlab.com/development/database/avoiding_downtime_in_migrations/) - maintained examples of multi-release and background migration practices.
- [Stripe: Online migrations at scale](https://stripe.com/blog/online-migrations) - a production account of dual writes, backfilling and controlled switching.
- [PostgreSQL: `CREATE INDEX`](https://www.postgresql.org/docs/current/sql-createindex.html) - one product's trade-offs and failure states for concurrent index creation.

## Non-relational databases, consistency and the data lifecycle

*Choose a store from the shape, access patterns, guarantees and lifecycle of the data—not from a category label.*

### What they are

**Non-relational** or **NoSQL** groups several unlike data models. Document, key-value, graph, time-series and search stores emphasise different shapes and access patterns. Categories overlap: a relational database can store JSON documents, while a product described as key-value may expose richer data structures. The label alone does not state the store's transactions, durability, scaling or read guarantees.

A useful decision model begins with four questions:

1. **Shape:** are the important facts tabular, nested, connected as a graph, ordered in time or prepared for search?
2. **Access patterns:** which reads and writes must be direct, and which relationships or aggregations must be computed?
3. **Guarantees:** which invariants, atomic changes, read freshness and failure behaviour does the product require?
4. **Lifecycle:** how is the data created, changed, retained, archived and deleted over time?

An order can use related SQL tables or one document with embedded line-item snapshots. The document may make a common read direct, but repeated product details need a rule: should old orders preserve purchase-time names and prices or follow the current product? Neither shape is universally more modern or scalable.

Consistency guarantees are product- and operation-specific. A non-relational store can offer transactions or reads guaranteed to return the latest completed write. A relational service can send some reads to additional copies called replicas, which may briefly return an older committed version. Chapter 6 explains the mechanisms. Here, ACID consistency means preserving valid database state, while **read consistency** describes which committed version a reader may observe.

The data lifecycle applies to every store. A delete button, a flag that hides rather than removes a record (often called a soft delete), an expiry timestamp, asynchronous removal and verified erasure are different behaviours. Archiving is not backup, and hiding a record does not prove it has left every index, log or retained copy. Recovery mechanisms belong in Chapter 8 and legal duties in Chapter 11.

### Why a builder needs to know this

Storage choice creates long-lived constraints on queries, integrity, operations and change. This model helps a builder compare actual requirements instead of choosing from a vendor catalogue or assuming that one database category determines every guarantee. Products such as PostgreSQL, MongoDB, Redis, DynamoDB and Firestore illustrate overlapping categories, not a ranking or universal shortlist. Product descriptions and guarantees were reviewed 2026-07-18 and must be checked for the chosen operation and deployment.

### Pitfalls

- **“Schemaless means no schema work.”** Expected structure moves into code, validation, indexes and operating practice.
- **“NoSQL means eventual consistency.”** Read and transaction guarantees depend on the product and operation.
- **“Relational means it cannot scale.”** Scale follows workload, architecture and operation, not a category slogan.
- **“Expiry deletes data immediately.”** Many expiry mechanisms make records eligible for later asynchronous removal.
- **“Lifecycle is a compliance add-on.”** Retention and deletion behaviour affect product correctness and cost even before legal duties are considered.

### Related concepts in TFB

- [Abstraction, information hiding and interfaces](03-software-engineering.md#abstraction-information-hiding-and-interfaces) - storage products with similar operations can make materially different behavioural promises.
- [Client-server systems and behavioural contracts](04-internet-web-and-apis.md#client-server-systems-network-service-application-programming-interfaces-and-behavioural-contracts) - remote data services expose failure and consistency as part of their contract.
- [Processors, memory and persistent storage](01-computing-foundations.md#processors-memory-and-persistent-storage) - every store ultimately depends on defined persistence and failure boundaries.

### Deeper concepts

- Document, key-value, graph, time-series and search models - the mechanics and trade-offs of each specialised shape.
- Operational and analytical stores - separating live product workloads from large-scale analysis.
- Retention, archival and legal holds - policies and mechanisms for preserving or removing data deliberately.

### Further reading

- [MongoDB: Data modelling](https://www.mongodb.com/docs/manual/data-modeling/) - first-party guidance on embedding, references and access-pattern trade-offs.
- [Amazon DynamoDB: Read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html) - an example of guarantees varying by operation in one product.
- [Cloud Firestore: Data model](https://firebase.google.com/docs/firestore/data-model) - a document and collection model whose structure still affects querying.
- [Redis: Data types](https://redis.io/docs/latest/develop/data-types/) - an example of a product that crosses simple category labels.

## Chapter status

The Chapter 5 first-pass draft covers the seven entries selected in the approved outline. It is awaiting owner approval. Further data-model, database-performance, concurrency, analytical-processing and lifecycle material remains optional and will be added only where it improves awareness without overloading the main traversal.

[Return to the guide map](../README.md#map-of-the-territory) · [Browse the complete Chapter 5 plan](../OUTLINE.md#5-data-and-databases)
