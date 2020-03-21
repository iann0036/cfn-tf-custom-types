# Terraform::RunScope::Step

CloudFormation equivalent of runscope_step

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::RunScope::Step",
    "Properties" : {
        "<a href="#beforescripts" title="BeforeScripts">BeforeScripts</a>" : <i>[ String, ... ]</i>,
        "<a href="#body" title="Body">Body</a>" : <i>String</i>,
        "<a href="#bucketid" title="BucketId">BucketId</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#method" title="Method">Method</a>" : <i>String</i>,
        "<a href="#note" title="Note">Note</a>" : <i>String</i>,
        "<a href="#scripts" title="Scripts">Scripts</a>" : <i>[ String, ... ]</i>,
        "<a href="#steptype" title="StepType">StepType</a>" : <i>String</i>,
        "<a href="#testid" title="TestId">TestId</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#assertions" title="Assertions">Assertions</a>" : <i>[ &lt;a href=&#34;assertions.md&#34;&gt;Assertions&lt;/a&gt;, ... ]</i>,
        "<a href="#auth" title="Auth">Auth</a>" : <i>[ &lt;a href=&#34;auth.md&#34;&gt;Auth&lt;/a&gt;, ... ]</i>,
        "<a href="#headers" title="Headers">Headers</a>" : <i>[ &lt;a href=&#34;headers.md&#34;&gt;Headers&lt;/a&gt;, ... ]</i>,
        "<a href="#variables" title="Variables">Variables</a>" : <i>[ &lt;a href=&#34;variables.md&#34;&gt;Variables&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::RunScope::Step
Properties:
    <a href="#beforescripts" title="BeforeScripts">BeforeScripts</a>: <i>
      - String</i>
    <a href="#body" title="Body">Body</a>: <i>String</i>
    <a href="#bucketid" title="BucketId">BucketId</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#method" title="Method">Method</a>: <i>String</i>
    <a href="#note" title="Note">Note</a>: <i>String</i>
    <a href="#scripts" title="Scripts">Scripts</a>: <i>
      - String</i>
    <a href="#steptype" title="StepType">StepType</a>: <i>String</i>
    <a href="#testid" title="TestId">TestId</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#assertions" title="Assertions">Assertions</a>: <i>
      - &lt;a href=&#34;assertions.md&#34;&gt;Assertions&lt;/a&gt;</i>
    <a href="#auth" title="Auth">Auth</a>: <i>
      - &lt;a href=&#34;auth.md&#34;&gt;Auth&lt;/a&gt;</i>
    <a href="#headers" title="Headers">Headers</a>: <i>
      - &lt;a href=&#34;headers.md&#34;&gt;Headers&lt;/a&gt;</i>
    <a href="#variables" title="Variables">Variables</a>: <i>
      - &lt;a href=&#34;variables.md&#34;&gt;Variables&lt;/a&gt;</i>
</pre>

## Properties

#### BeforeScripts

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Body

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Note

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scripts

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StepType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Assertions

_Required_: No

_Type_: List of &lt;a href=&#34;assertions.md&#34;&gt;Assertions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Auth

_Required_: No

_Type_: List of &lt;a href=&#34;auth.md&#34;&gt;Auth&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No

_Type_: List of &lt;a href=&#34;headers.md&#34;&gt;Headers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variables

_Required_: No

_Type_: List of &lt;a href=&#34;variables.md&#34;&gt;Variables&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

