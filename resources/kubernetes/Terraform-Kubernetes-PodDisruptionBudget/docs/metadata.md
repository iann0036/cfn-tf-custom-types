# Terraform::Kubernetes::PodDisruptionBudget Metadata

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ &lt;a href=&#34;metadata-annotations.md&#34;&gt;Annotations&lt;/a&gt;, ... ]</i>,
    "<a href="#generatename" title="GenerateName">GenerateName</a>" : <i>String</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ &lt;a href=&#34;metadata-labels.md&#34;&gt;Labels&lt;/a&gt;, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#annotations" title="Annotations">Annotations</a>: <i>
      - &lt;a href=&#34;metadata-annotations.md&#34;&gt;Annotations&lt;/a&gt;</i>
<a href="#generatename" title="GenerateName">GenerateName</a>: <i>String</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - &lt;a href=&#34;metadata-labels.md&#34;&gt;Labels&lt;/a&gt;</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
</pre>

## Properties

#### Annotations

_Required_: No
_Type_: List of &lt;a href=&#34;metadata-annotations.md&#34;&gt;Annotations&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GenerateName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No
_Type_: List of &lt;a href=&#34;metadata-labels.md&#34;&gt;Labels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

