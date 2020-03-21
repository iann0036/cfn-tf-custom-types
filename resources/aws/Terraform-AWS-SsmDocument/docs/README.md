# Terraform::AWS::SsmDocument

CloudFormation equivalent of aws_ssm_document

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SsmDocument",
    "Properties" : {
        "<a href="#content" title="Content">Content</a>" : <i>String</i>,
        "<a href="#documentformat" title="DocumentFormat">DocumentFormat</a>" : <i>String</i>,
        "<a href="#documenttype" title="DocumentType">DocumentType</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>[ &lt;a href=&#34;permissions.md&#34;&gt;Permissions&lt;/a&gt;, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#targettype" title="TargetType">TargetType</a>" : <i>String</i>,
        "<a href="#attachmentssource" title="AttachmentsSource">AttachmentsSource</a>" : <i>[ &lt;a href=&#34;attachmentssource.md&#34;&gt;AttachmentsSource&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SsmDocument
Properties:
    <a href="#content" title="Content">Content</a>: <i>String</i>
    <a href="#documentformat" title="DocumentFormat">DocumentFormat</a>: <i>String</i>
    <a href="#documenttype" title="DocumentType">DocumentType</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>
      - &lt;a href=&#34;permissions.md&#34;&gt;Permissions&lt;/a&gt;</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#targettype" title="TargetType">TargetType</a>: <i>String</i>
    <a href="#attachmentssource" title="AttachmentsSource">AttachmentsSource</a>: <i>
      - &lt;a href=&#34;attachmentssource.md&#34;&gt;AttachmentsSource&lt;/a&gt;</i>
</pre>

## Properties

#### Content

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DocumentFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DocumentType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

_Required_: No

_Type_: List of &lt;a href=&#34;permissions.md&#34;&gt;Permissions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachmentsSource

_Required_: No

_Type_: List of &lt;a href=&#34;attachmentssource.md&#34;&gt;AttachmentsSource&lt;/a&gt;

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

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### CreatedDate

Returns the &lt;code&gt;CreatedDate&lt;/code&gt; value.

#### DefaultVersion

Returns the &lt;code&gt;DefaultVersion&lt;/code&gt; value.

#### Description

Returns the &lt;code&gt;Description&lt;/code&gt; value.

#### Hash

Returns the &lt;code&gt;Hash&lt;/code&gt; value.

#### HashType

Returns the &lt;code&gt;HashType&lt;/code&gt; value.

#### LatestVersion

Returns the &lt;code&gt;LatestVersion&lt;/code&gt; value.

#### Owner

Returns the &lt;code&gt;Owner&lt;/code&gt; value.

#### Parameter

Returns the &lt;code&gt;Parameter&lt;/code&gt; value.

#### PlatformTypes

Returns the &lt;code&gt;PlatformTypes&lt;/code&gt; value.

#### SchemaVersion

Returns the &lt;code&gt;SchemaVersion&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

