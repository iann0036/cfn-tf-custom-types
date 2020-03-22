# Terraform::PostgreSQL::Role

The ``postgresql_role`` resource creates and manages a role on a PostgreSQL
server.

When a ``postgresql_role`` resource is removed, the PostgreSQL ROLE will
automatically run a [`REASSIGN
OWNED`](https://www.postgresql.org/docs/current/static/sql-reassign-owned.html)
and [`DROP
OWNED`](https://www.postgresql.org/docs/current/static/sql-drop-owned.html) to
the `CURRENT_USER` (normally the connected user for the provider).  If the
specified PostgreSQL ROLE owns objects in multiple PostgreSQL databases in the
same PostgreSQL Cluster, one PostgreSQL provider per database must be created
and all but the final ``postgresql_role`` must specify a `skip_drop_role`.

~> **Note:** All arguments including role name and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::PostgreSQL::Role",
    "Properties" : {
        "<a href="#bypassrowlevelsecurity" title="BypassRowLevelSecurity">BypassRowLevelSecurity</a>" : <i>Boolean</i>,
        "<a href="#connectionlimit" title="ConnectionLimit">ConnectionLimit</a>" : <i>Double</i>,
        "<a href="#createdatabase" title="CreateDatabase">CreateDatabase</a>" : <i>Boolean</i>,
        "<a href="#createrole" title="CreateRole">CreateRole</a>" : <i>Boolean</i>,
        "<a href="#encrypted" title="Encrypted">Encrypted</a>" : <i>String</i>,
        "<a href="#encryptedpassword" title="EncryptedPassword">EncryptedPassword</a>" : <i>Boolean</i>,
        "<a href="#inherit" title="Inherit">Inherit</a>" : <i>Boolean</i>,
        "<a href="#login" title="Login">Login</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#replication" title="Replication">Replication</a>" : <i>Boolean</i>,
        "<a href="#roles" title="Roles">Roles</a>" : <i>[ String, ... ]</i>,
        "<a href="#searchpath" title="SearchPath">SearchPath</a>" : <i>[ String, ... ]</i>,
        "<a href="#skipdroprole" title="SkipDropRole">SkipDropRole</a>" : <i>Boolean</i>,
        "<a href="#skipreassignowned" title="SkipReassignOwned">SkipReassignOwned</a>" : <i>Boolean</i>,
        "<a href="#statementtimeout" title="StatementTimeout">StatementTimeout</a>" : <i>Double</i>,
        "<a href="#superuser" title="Superuser">Superuser</a>" : <i>Boolean</i>,
        "<a href="#validuntil" title="ValidUntil">ValidUntil</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::PostgreSQL::Role
Properties:
    <a href="#bypassrowlevelsecurity" title="BypassRowLevelSecurity">BypassRowLevelSecurity</a>: <i>Boolean</i>
    <a href="#connectionlimit" title="ConnectionLimit">ConnectionLimit</a>: <i>Double</i>
    <a href="#createdatabase" title="CreateDatabase">CreateDatabase</a>: <i>Boolean</i>
    <a href="#createrole" title="CreateRole">CreateRole</a>: <i>Boolean</i>
    <a href="#encrypted" title="Encrypted">Encrypted</a>: <i>String</i>
    <a href="#encryptedpassword" title="EncryptedPassword">EncryptedPassword</a>: <i>Boolean</i>
    <a href="#inherit" title="Inherit">Inherit</a>: <i>Boolean</i>
    <a href="#login" title="Login">Login</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#replication" title="Replication">Replication</a>: <i>Boolean</i>
    <a href="#roles" title="Roles">Roles</a>: <i>
      - String</i>
    <a href="#searchpath" title="SearchPath">SearchPath</a>: <i>
      - String</i>
    <a href="#skipdroprole" title="SkipDropRole">SkipDropRole</a>: <i>Boolean</i>
    <a href="#skipreassignowned" title="SkipReassignOwned">SkipReassignOwned</a>: <i>Boolean</i>
    <a href="#statementtimeout" title="StatementTimeout">StatementTimeout</a>: <i>Double</i>
    <a href="#superuser" title="Superuser">Superuser</a>: <i>Boolean</i>
    <a href="#validuntil" title="ValidUntil">ValidUntil</a>: <i>String</i>
</pre>

## Properties

#### BypassRowLevelSecurity

Defines whether a role bypasses every
row-level security (RLS) policy.  Default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionLimit

If this role can log in, this specifies how
many concurrent connections the role can establish. `-1` (the default) means no
limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateDatabase

Defines a role's ability to execute `CREATE
DATABASE`.  Default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateRole

Defines a role's ability to execute `CREATE ROLE`.
A role with this privilege can also alter and drop other roles.  Default value
is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encrypted

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptedPassword

Defines whether the password is stored
encrypted in the system catalogs.  Default value is `true`.  NOTE: this value
is always set (to the conservative and safe value), but may interfere with the
behavior of
[PostgreSQL's `password_encryption` setting](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inherit

Defines whether a role "inherits" the privileges of
roles it is a member of.  Default value is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Login

Defines whether role is allowed to log in.  Roles without
this attribute are useful for managing database privileges, but are not users
in the usual sense of the word.  Default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the role. Must be unique on the PostgreSQL
server instance where it is configured.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Sets the role's password. A password is only of use
for roles having the `login` attribute set to true.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replication

Defines whether a role is allowed to initiate
streaming replication or put the system in and out of backup mode.  Default
value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Roles

Defines list of roles which will be granted to this new role.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchPath

Alters the search path of this new role. Note that
due to limitations in the implementation, values cannot contain the substring
`", "`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipDropRole

When a PostgreSQL ROLE exists in multiple
databases and the ROLE is dropped, the
[cleanup of ownership of objects](https://www.postgresql.org/docs/current/static/role-removal.html)
in each of the respective databases must occur before the ROLE can be dropped
from the catalog.  Set this option to true when there are multiple databases
in a PostgreSQL cluster using the same PostgreSQL ROLE for object ownership.
This is the third and final step taken when removing a ROLE from a database.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipReassignOwned

When a PostgreSQL ROLE exists in multiple
databases and the ROLE is dropped, a
[`REASSIGN OWNED`](https://www.postgresql.org/docs/current/static/sql-reassign-owned.html) in
must be executed on each of the respective databases before the `DROP ROLE`
can be executed to dropped the ROLE from the catalog.  This is the first and
second steps taken when removing a ROLE from a database (the second step being
an implicit
[`DROP OWNED`](https://www.postgresql.org/docs/current/static/sql-drop-owned.html)).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatementTimeout

Defines [`statement_timeout`](https://www.postgresql.org/docs/current/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT) setting for this role which allows to abort any statement that takes more than the specified amount of time.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Superuser

Defines whether the role is a "superuser", and
therefore can override all access restrictions within the database.  Default
value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidUntil

Defines the date and time after which the role's
password is no longer valid.  Established connections past this `valid_time`
will have to be manually terminated.  This value corresponds to a PostgreSQL
datetime. If omitted or the magic value `NULL` is used, `valid_until` will be
set to `infinity`.  Default is `NULL`, therefore `infinity`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

