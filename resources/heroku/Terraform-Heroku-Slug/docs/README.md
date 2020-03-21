# Terraform::Heroku::Slug

CloudFormation equivalent of heroku_slug

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::Slug",
    "Properties" : {
        "<a href="#app" title="App">App</a>" : <i>String</i>,
        "<a href="#buildpackprovideddescription" title="BuildpackProvidedDescription">BuildpackProvidedDescription</a>" : <i>String</i>,
        "<a href="#checksum" title="Checksum">Checksum</a>" : <i>String</i>,
        "<a href="#commit" title="Commit">Commit</a>" : <i>String</i>,
        "<a href="#commitdescription" title="CommitDescription">CommitDescription</a>" : <i>String</i>,
        "<a href="#filepath" title="FilePath">FilePath</a>" : <i>String</i>,
        "<a href="#fileurl" title="FileUrl">FileUrl</a>" : <i>String</i>,
        "<a href="#processtypes" title="ProcessTypes">ProcessTypes</a>" : <i>[ <a href="processtypes.md">ProcessTypes</a>, ... ]</i>,
        "<a href="#stack" title="Stack">Stack</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::Slug
Properties:
    <a href="#app" title="App">App</a>: <i>String</i>
    <a href="#buildpackprovideddescription" title="BuildpackProvidedDescription">BuildpackProvidedDescription</a>: <i>String</i>
    <a href="#checksum" title="Checksum">Checksum</a>: <i>String</i>
    <a href="#commit" title="Commit">Commit</a>: <i>String</i>
    <a href="#commitdescription" title="CommitDescription">CommitDescription</a>: <i>String</i>
    <a href="#filepath" title="FilePath">FilePath</a>: <i>String</i>
    <a href="#fileurl" title="FileUrl">FileUrl</a>: <i>String</i>
    <a href="#processtypes" title="ProcessTypes">ProcessTypes</a>: <i>
      - <a href="processtypes.md">ProcessTypes</a></i>
    <a href="#stack" title="Stack">Stack</a>: <i>String</i>
</pre>

## Properties

#### App

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildpackProvidedDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Checksum

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Commit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommitDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessTypes

_Required_: Yes

_Type_: List of <a href="processtypes.md">ProcessTypes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stack

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

#### Blob

Returns the <code>Blob</code> value.

#### Size

Returns the <code>Size</code> value.

#### StackId

Returns the <code>StackId</code> value.

