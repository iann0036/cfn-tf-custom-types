# TF::AWS::DbProxyDefaultTargetGroup ConnectionPoolConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#connectionborrowtimeout" title="ConnectionBorrowTimeout">ConnectionBorrowTimeout</a>" : <i>Double</i>,
    "<a href="#initquery" title="InitQuery">InitQuery</a>" : <i>String</i>,
    "<a href="#maxconnectionspercent" title="MaxConnectionsPercent">MaxConnectionsPercent</a>" : <i>Double</i>,
    "<a href="#maxidleconnectionspercent" title="MaxIdleConnectionsPercent">MaxIdleConnectionsPercent</a>" : <i>Double</i>,
    "<a href="#sessionpinningfilters" title="SessionPinningFilters">SessionPinningFilters</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#connectionborrowtimeout" title="ConnectionBorrowTimeout">ConnectionBorrowTimeout</a>: <i>Double</i>
<a href="#initquery" title="InitQuery">InitQuery</a>: <i>String</i>
<a href="#maxconnectionspercent" title="MaxConnectionsPercent">MaxConnectionsPercent</a>: <i>Double</i>
<a href="#maxidleconnectionspercent" title="MaxIdleConnectionsPercent">MaxIdleConnectionsPercent</a>: <i>Double</i>
<a href="#sessionpinningfilters" title="SessionPinningFilters">SessionPinningFilters</a>: <i>
      - String</i>
</pre>

## Properties

#### ConnectionBorrowTimeout

The number of seconds for a proxy to wait for a connection to become available in the connection pool. Only applies when the proxy has opened its maximum number of connections and all connections are busy with client sessions.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitQuery

One or more SQL statements for the proxy to run when opening each new database connection. Typically used with `SET` statements to make sure that each connection has identical settings such as time zone and character set. This setting is empty by default. For multiple statements, use semicolons as the separator. You can also include multiple variables in a single `SET` statement, such as `SET x=1, y=2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConnectionsPercent

The maximum size of the connection pool for each target in a target group. For Aurora MySQL, it is expressed as a percentage of the max_connections setting for the RDS DB instance or Aurora DB cluster used by the target group.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxIdleConnectionsPercent

Controls how actively the proxy closes idle database connections in the connection pool. A high value enables the proxy to leave a high percentage of idle connections open. A low value causes the proxy to close idle client connections and return the underlying database connections to the connection pool. For Aurora MySQL, it is expressed as a percentage of the max_connections setting for the RDS DB instance or Aurora DB cluster used by the target group.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionPinningFilters

Each item in the list represents a class of SQL operations that normally cause all later statements in a session using a proxy to be pinned to the same underlying database connection. Including an item in the list exempts that class of SQL operations from the pinning behavior. Currently, the only allowed value is `EXCLUDE_VARIABLE_SETS`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

