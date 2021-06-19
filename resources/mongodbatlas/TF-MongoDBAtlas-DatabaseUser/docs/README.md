# TF::MongoDBAtlas::DatabaseUser

`mongodbatlas_database_user` provides a Database User resource. This represents a database user which will be applied to all clusters within the project.

Each user has a set of roles that provide access to the project’s databases. User's roles apply to all the clusters in the project: if two clusters have a `products` database and a user has a role granting `read` access on the products database, the user has that access on both clusters.

-> **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.

~> **IMPORTANT:** All arguments including the password will be stored in the raw state as plain-text. [Read more about sensitive data in state.](https://www.terraform.io/docs/state/sensitive-data.html)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::DatabaseUser",
    "Properties" : {
        "<a href="#authdatabasename" title="AuthDatabaseName">AuthDatabaseName</a>" : <i>String</i>,
        "<a href="#awsiamtype" title="AwsIamType">AwsIamType</a>" : <i>String</i>,
        "<a href="#databasename" title="DatabaseName">DatabaseName</a>" : <i>String</i>,
        "<a href="#ldapauthtype" title="LdapAuthType">LdapAuthType</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#x509type" title="X509Type">X509Type</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#roles" title="Roles">Roles</a>" : <i>[ <a href="rolesdefinition.md">RolesDefinition</a>, ... ]</i>,
        "<a href="#scopes" title="Scopes">Scopes</a>" : <i>[ <a href="scopesdefinition.md">ScopesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::DatabaseUser
Properties:
    <a href="#authdatabasename" title="AuthDatabaseName">AuthDatabaseName</a>: <i>String</i>
    <a href="#awsiamtype" title="AwsIamType">AwsIamType</a>: <i>String</i>
    <a href="#databasename" title="DatabaseName">DatabaseName</a>: <i>String</i>
    <a href="#ldapauthtype" title="LdapAuthType">LdapAuthType</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#x509type" title="X509Type">X509Type</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#roles" title="Roles">Roles</a>: <i>
      - <a href="rolesdefinition.md">RolesDefinition</a></i>
    <a href="#scopes" title="Scopes">Scopes</a>: <i>
      - <a href="scopesdefinition.md">ScopesDefinition</a></i>
</pre>

## Properties

#### AuthDatabaseName

Database against which Atlas authenticates the user. A user must provide both a username and authentication database to log into MongoDB.
Accepted values include:
* `admin` if `x509_type` and `aws_iam_type` are omitted or NONE.
* `$external` if `x509_type` is MANAGED or CUSTOMER or `aws_iam_type` is USER or ROLE.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsIamType

If this value is set, the new database user authenticates with AWS IAM credentials. If no value is given, Atlas uses the default value of NONE. The accepted types are:
* `NONE` -	The user does not use AWS IAM credentials.
* `USER` - New database user has AWS IAM user credentials.
* `ROLE` -  New database user has credentials associated with an AWS IAM role.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapAuthType

Method by which the provided `username` is authenticated. If no value is given, Atlas uses the default value of `NONE`.
* `NONE` -	Atlas authenticates this user through [SCRAM-SHA](https://docs.mongodb.com/manual/core/security-scram/), not LDAP.
* `USER` - LDAP server authenticates this user through the user's LDAP user. `username` must also be a fully qualified distinguished name, as defined in [RFC-2253](https://tools.ietf.org/html/rfc2253).
* `GROUP` - LDAP server authenticates this user using their LDAP user and authorizes this user using their LDAP group. To learn more about LDAP security, see [Set up User Authentication and Authorization with LDAP](https://docs.atlas.mongodb.com/security-ldaps). `username` must also be a fully qualified distinguished name, as defined in [RFC-2253](https://tools.ietf.org/html/rfc2253).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

User's initial password. A value is required to create the database user, however the argument but may be removed from your Terraform configuration after user creation without impacting the user, password or Terraform management. IMPORTANT --- Passwords may show up in Terraform related logs and it will be stored in the Terraform state file as plain-text. Password can be changed after creation using your preferred method, e.g. via the MongoDB Atlas UI, to ensure security.  If you do change management of the password to outside of Terraform be sure to remove the argument from the Terraform configuration so it is not inadvertently updated to the original password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The unique ID for the project to create the database user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

Username for authenticating to MongoDB. USER_ARN or ROLE_ARN if `aws_iam_type` is USER or ROLE.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### X509Type

X.509 method by which the provided username is authenticated. If no value is given, Atlas uses the default value of NONE. The accepted types are:
* `NONE` -	The user does not use X.509 authentication.
* `MANAGED` - The user is being created for use with Atlas-managed X.509.Externally authenticated users can only be created on the `$external` database.
* `CUSTOMER` -  The user is being created for use with Self-Managed X.509. Users created with this x509Type require a Common Name (CN) in the username field. Externally authenticated users can only be created on the `$external` database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Roles

_Required_: No

_Type_: List of <a href="rolesdefinition.md">RolesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scopes

_Required_: No

_Type_: List of <a href="scopesdefinition.md">ScopesDefinition</a>

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

