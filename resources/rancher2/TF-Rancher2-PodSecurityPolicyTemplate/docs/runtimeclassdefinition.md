# TF::Rancher2::PodSecurityPolicyTemplate RuntimeClassDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedruntimeclassnames" title="AllowedRuntimeClassNames">AllowedRuntimeClassNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#defaultruntimeclassname" title="DefaultRuntimeClassName">DefaultRuntimeClassName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allowedruntimeclassnames" title="AllowedRuntimeClassNames">AllowedRuntimeClassNames</a>: <i>
      - String</i>
<a href="#defaultruntimeclassname" title="DefaultRuntimeClassName">DefaultRuntimeClassName</a>: <i>String</i>
</pre>

## Properties

#### AllowedRuntimeClassNames

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRuntimeClassName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

