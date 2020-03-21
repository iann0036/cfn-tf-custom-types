# Terraform::Heroku::Slug

CloudFormation equivalent of heroku_slug

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::Slug",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#app" title="App">App</a>" : <i>String</i>,
        "<a href="#blob" title="Blob">Blob</a>" : <i>[ &lt;a href=&#34;blob.md&#34;&gt;Blob&lt;/a&gt;, ... ]</i>,
        "<a href="#buildpackprovideddescription" title="BuildpackProvidedDescription">BuildpackProvidedDescription</a>" : <i>String</i>,
        "<a href="#checksum" title="Checksum">Checksum</a>" : <i>String</i>,
        "<a href="#commit" title="Commit">Commit</a>" : <i>String</i>,
        "<a href="#commitdescription" title="CommitDescription">CommitDescription</a>" : <i>String</i>,
        "<a href="#filepath" title="FilePath">FilePath</a>" : <i>String</i>,
        "<a href="#fileurl" title="FileUrl">FileUrl</a>" : <i>String</i>,
        "<a href="#processtypes" title="ProcessTypes">ProcessTypes</a>" : <i>[ &lt;a href=&#34;processtypes.md&#34;&gt;ProcessTypes&lt;/a&gt;, ... ]</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#stack" title="Stack">Stack</a>" : <i>String</i>,
        "<a href="#stackid" title="StackId">StackId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::Slug
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#app" title="App">App</a>: <i>String</i>
    <a href="#blob" title="Blob">Blob</a>: <i>
      - &lt;a href=&#34;blob.md&#34;&gt;Blob&lt;/a&gt;</i>
    <a href="#buildpackprovideddescription" title="BuildpackProvidedDescription">BuildpackProvidedDescription</a>: <i>String</i>
    <a href="#checksum" title="Checksum">Checksum</a>: <i>String</i>
    <a href="#commit" title="Commit">Commit</a>: <i>String</i>
    <a href="#commitdescription" title="CommitDescription">CommitDescription</a>: <i>String</i>
    <a href="#filepath" title="FilePath">FilePath</a>: <i>String</i>
    <a href="#fileurl" title="FileUrl">FileUrl</a>: <i>String</i>
    <a href="#processtypes" title="ProcessTypes">ProcessTypes</a>: <i>
      - &lt;a href=&#34;processtypes.md&#34;&gt;ProcessTypes&lt;/a&gt;</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#stack" title="Stack">Stack</a>: <i>String</i>
    <a href="#stackid" title="StackId">StackId</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### App

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Blob

_Required_: No

_Type_: List of &lt;a href=&#34;blob.md&#34;&gt;Blob&lt;/a&gt;

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

_Type_: List of &lt;a href=&#34;processtypes.md&#34;&gt;ProcessTypes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stack

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackId

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

Returns the &lt;code&gt;Blob&lt;/code&gt; value.

#### Size

Returns the &lt;code&gt;Size&lt;/code&gt; value.

#### StackId

Returns the &lt;code&gt;StackId&lt;/code&gt; value.

