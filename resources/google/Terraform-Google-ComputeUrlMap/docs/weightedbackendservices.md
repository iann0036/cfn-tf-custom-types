# Terraform::Google::ComputeUrlMap WeightedBackendServices

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backendservice" title="BackendService">BackendService</a>" : <i>String</i>,
    "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>,
    "<a href="#headeraction" title="HeaderAction">HeaderAction</a>" : <i>[ &lt;a href=&#34;weightedbackendservices-headeraction.md&#34;&gt;HeaderAction&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#backendservice" title="BackendService">BackendService</a>: <i>String</i>
<a href="#weight" title="Weight">Weight</a>: <i>Double</i>
<a href="#headeraction" title="HeaderAction">HeaderAction</a>: <i>
      - &lt;a href=&#34;weightedbackendservices-headeraction.md&#34;&gt;HeaderAction&lt;/a&gt;</i>
</pre>

## Properties

#### BackendService

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderAction

_Required_: No
_Type_: List of &lt;a href=&#34;weightedbackendservices-headeraction.md&#34;&gt;HeaderAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

