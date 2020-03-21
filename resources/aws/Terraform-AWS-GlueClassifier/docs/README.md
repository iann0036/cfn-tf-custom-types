# Terraform::AWS::GlueClassifier

CloudFormation equivalent of aws_glue_classifier

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::GlueClassifier",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#csvclassifier" title="CsvClassifier">CsvClassifier</a>" : <i>[ &lt;a href=&#34;csvclassifier.md&#34;&gt;CsvClassifier&lt;/a&gt;, ... ]</i>,
        "<a href="#grokclassifier" title="GrokClassifier">GrokClassifier</a>" : <i>[ &lt;a href=&#34;grokclassifier.md&#34;&gt;GrokClassifier&lt;/a&gt;, ... ]</i>,
        "<a href="#jsonclassifier" title="JsonClassifier">JsonClassifier</a>" : <i>[ &lt;a href=&#34;jsonclassifier.md&#34;&gt;JsonClassifier&lt;/a&gt;, ... ]</i>,
        "<a href="#xmlclassifier" title="XmlClassifier">XmlClassifier</a>" : <i>[ &lt;a href=&#34;xmlclassifier.md&#34;&gt;XmlClassifier&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::GlueClassifier
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#csvclassifier" title="CsvClassifier">CsvClassifier</a>: <i>
      - &lt;a href=&#34;csvclassifier.md&#34;&gt;CsvClassifier&lt;/a&gt;</i>
    <a href="#grokclassifier" title="GrokClassifier">GrokClassifier</a>: <i>
      - &lt;a href=&#34;grokclassifier.md&#34;&gt;GrokClassifier&lt;/a&gt;</i>
    <a href="#jsonclassifier" title="JsonClassifier">JsonClassifier</a>: <i>
      - &lt;a href=&#34;jsonclassifier.md&#34;&gt;JsonClassifier&lt;/a&gt;</i>
    <a href="#xmlclassifier" title="XmlClassifier">XmlClassifier</a>: <i>
      - &lt;a href=&#34;xmlclassifier.md&#34;&gt;XmlClassifier&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsvClassifier

_Required_: No

_Type_: List of &lt;a href=&#34;csvclassifier.md&#34;&gt;CsvClassifier&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrokClassifier

_Required_: No

_Type_: List of &lt;a href=&#34;grokclassifier.md&#34;&gt;GrokClassifier&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsonClassifier

_Required_: No

_Type_: List of &lt;a href=&#34;jsonclassifier.md&#34;&gt;JsonClassifier&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XmlClassifier

_Required_: No

_Type_: List of &lt;a href=&#34;xmlclassifier.md&#34;&gt;XmlClassifier&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

