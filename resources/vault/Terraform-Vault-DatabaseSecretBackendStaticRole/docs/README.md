# Terraform::Vault::DatabaseSecretBackendStaticRole

Creates a Database Secret Backend static role in Vault. Database secret backend
static roles can be used to manage 1-to-1 mapping of a Vault Role to a user in a
database for the database.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::DatabaseSecretBackendStaticRole",
    "Properties" : {
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#dbname" title="DbName">DbName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rotationperiod" title="RotationPeriod">RotationPeriod</a>" : <i>Double</i>,
        "<a href="#rotationstatements" title="RotationStatements">RotationStatements</a>" : <i>[ String, ... ]</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::DatabaseSecretBackendStaticRole
Properties:
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#dbname" title="DbName">DbName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rotationperiod" title="RotationPeriod">RotationPeriod</a>: <i>Double</i>
    <a href="#rotationstatements" title="RotationStatements">RotationStatements</a>: <i>
      - String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### Backend

The unique name of the Vault mount to configure.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbName

The unique name of the database connection to use for the static role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name to give the static role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationPeriod

The amount of time Vault should wait before rotating the password, in seconds.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationStatements

Database statements to execute to rotate the password for the configured database user.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The database username that this static role corresponds to.

_Required_: Yes

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

