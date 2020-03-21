# Terraform::Alicloud::LogStoreIndex

CloudFormation equivalent of alicloud_log_store_index

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::LogStoreIndex",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#logstore" title="Logstore">Logstore</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#fieldsearch" title="FieldSearch">FieldSearch</a>" : <i>[ &lt;a href=&#34;fieldsearch.md&#34;&gt;FieldSearch&lt;/a&gt;, ... ]</i>,
        "<a href="#fulltext" title="FullText">FullText</a>" : <i>[ &lt;a href=&#34;fulltext.md&#34;&gt;FullText&lt;/a&gt;, ... ]</i>,
        "<a href="#jsonkeys" title="JsonKeys">JsonKeys</a>" : <i>[ &lt;a href=&#34;jsonkeys.md&#34;&gt;JsonKeys&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::LogStoreIndex
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#logstore" title="Logstore">Logstore</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#fieldsearch" title="FieldSearch">FieldSearch</a>: <i>
      - &lt;a href=&#34;fieldsearch.md&#34;&gt;FieldSearch&lt;/a&gt;</i>
    <a href="#fulltext" title="FullText">FullText</a>: <i>
      - &lt;a href=&#34;fulltext.md&#34;&gt;FullText&lt;/a&gt;</i>
    <a href="#jsonkeys" title="JsonKeys">JsonKeys</a>: <i>
      - &lt;a href=&#34;jsonkeys.md&#34;&gt;JsonKeys&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logstore

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldSearch

_Required_: No

_Type_: List of &lt;a href=&#34;fieldsearch.md&#34;&gt;FieldSearch&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullText

_Required_: No

_Type_: List of &lt;a href=&#34;fulltext.md&#34;&gt;FullText&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsonKeys

_Required_: No

_Type_: List of &lt;a href=&#34;jsonkeys.md&#34;&gt;JsonKeys&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

