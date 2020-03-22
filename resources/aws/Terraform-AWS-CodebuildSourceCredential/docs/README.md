# Terraform::AWS::CodebuildSourceCredential

CloudFormation equivalent of aws_codebuild_source_credential

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CodebuildSourceCredential",
    "Properties" : {
        "<a href="#authtype" title="AuthType">AuthType</a>" : <i>String</i>,
        "<a href="#servertype" title="ServerType">ServerType</a>" : <i>String</i>,
        "<a href="#token" title="Token">Token</a>" : <i>String</i>,
        "<a href="#username" title="UserName">UserName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CodebuildSourceCredential
Properties:
    <a href="#authtype" title="AuthType">AuthType</a>: <i>String</i>
    <a href="#servertype" title="ServerType">ServerType</a>: <i>String</i>
    <a href="#token" title="Token">Token</a>: <i>String</i>
    <a href="#username" title="UserName">UserName</a>: <i>String</i>
</pre>

## Properties

#### AuthType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

