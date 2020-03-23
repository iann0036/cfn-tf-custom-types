# Terraform::AWS::CodebuildSourceCredential

Provides a CodeBuild Source Credentials Resource.

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

The type of authentication used to connect to a GitHub, GitHub Enterprise, or Bitbucket repository. An OAUTH connection is not supported by the API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerType

The source provider used for this project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

For `GitHub` or `GitHub Enterprise`, this is the personal access token. For `Bitbucket`, this is the app password.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserName

The Bitbucket username when the authType is `BASIC_AUTH`. This parameter is not valid for other types of source providers or connections.

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

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

