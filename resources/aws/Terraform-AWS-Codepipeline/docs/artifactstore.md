# Terraform::AWS::Codepipeline ArtifactStore

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>" : <i>[ &lt;a href=&#34;artifactstore-encryptionkey.md&#34;&gt;EncryptionKey&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>: <i>
      - &lt;a href=&#34;artifactstore-encryptionkey.md&#34;&gt;EncryptionKey&lt;/a&gt;</i>
</pre>

## Properties

#### Location

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionKey

_Required_: No
_Type_: List of &lt;a href=&#34;artifactstore-encryptionkey.md&#34;&gt;EncryptionKey&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

