# TF::AWS::OpsworksRdsDbInstance

Provides an OpsWorks RDS DB Instance resource.

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::OpsworksRdsDbInstance",
    "Properties" : {
        "<a href="#dbpassword" title="DbPassword">DbPassword</a>" : <i>String</i>,
        "<a href="#dbuser" title="DbUser">DbUser</a>" : <i>String</i>,
        "<a href="#rdsdbinstancearn" title="RdsDbInstanceArn">RdsDbInstanceArn</a>" : <i>String</i>,
        "<a href="#stackid" title="StackId">StackId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::OpsworksRdsDbInstance
Properties:
    <a href="#dbpassword" title="DbPassword">DbPassword</a>: <i>String</i>
    <a href="#dbuser" title="DbUser">DbUser</a>: <i>String</i>
    <a href="#rdsdbinstancearn" title="RdsDbInstanceArn">RdsDbInstanceArn</a>: <i>String</i>
    <a href="#stackid" title="StackId">StackId</a>: <i>String</i>
</pre>

## Properties

#### DbPassword

A db password.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbUser

A db username.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RdsDbInstanceArn

The db instance to register for this stack. Changing this will force a new resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackId

The stack to register a db instance for. Changing this will force a new resource.

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

#### Id

Returns the <code>Id</code> value.

