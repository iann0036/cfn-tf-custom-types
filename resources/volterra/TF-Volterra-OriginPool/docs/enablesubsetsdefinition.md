# TF::Volterra::OriginPool EnableSubsetsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#anyendpoint" title="AnyEndpoint">AnyEndpoint</a>" : <i>Boolean</i>,
    "<a href="#failrequest" title="FailRequest">FailRequest</a>" : <i>Boolean</i>,
    "<a href="#defaultsubset" title="DefaultSubset">DefaultSubset</a>" : <i>[ <a href="defaultsubsetdefinition.md">DefaultSubsetDefinition</a>, ... ]</i>,
    "<a href="#endpointsubsets" title="EndpointSubsets">EndpointSubsets</a>" : <i>[ <a href="endpointsubsetsdefinition.md">EndpointSubsetsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#anyendpoint" title="AnyEndpoint">AnyEndpoint</a>: <i>Boolean</i>
<a href="#failrequest" title="FailRequest">FailRequest</a>: <i>Boolean</i>
<a href="#defaultsubset" title="DefaultSubset">DefaultSubset</a>: <i>
      - <a href="defaultsubsetdefinition.md">DefaultSubsetDefinition</a></i>
<a href="#endpointsubsets" title="EndpointSubsets">EndpointSubsets</a>: <i>
      - <a href="endpointsubsetsdefinition.md">EndpointSubsetsDefinition</a></i>
</pre>

## Properties

#### AnyEndpoint

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailRequest

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultSubset

_Required_: No

_Type_: List of <a href="defaultsubsetdefinition.md">DefaultSubsetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointSubsets

_Required_: No

_Type_: List of <a href="endpointsubsetsdefinition.md">EndpointSubsetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

