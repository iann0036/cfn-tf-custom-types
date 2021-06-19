# TF::Volterra::TcpLoadbalancer OriginPoolsWeightsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#endpointsubsets" title="EndpointSubsets">EndpointSubsets</a>" : <i>[ <a href="endpointsubsetsdefinition.md">EndpointSubsetsDefinition</a>, ... ]</i>,
    "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>,
    "<a href="#cluster" title="Cluster">Cluster</a>" : <i>[ <a href="clusterdefinition.md">ClusterDefinition</a>, ... ]</i>,
    "<a href="#pool" title="Pool">Pool</a>" : <i>[ <a href="pooldefinition.md">PoolDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#endpointsubsets" title="EndpointSubsets">EndpointSubsets</a>: <i>
      - <a href="endpointsubsetsdefinition.md">EndpointSubsetsDefinition</a></i>
<a href="#weight" title="Weight">Weight</a>: <i>Double</i>
<a href="#cluster" title="Cluster">Cluster</a>: <i>
      - <a href="clusterdefinition.md">ClusterDefinition</a></i>
<a href="#pool" title="Pool">Pool</a>: <i>
      - <a href="pooldefinition.md">PoolDefinition</a></i>
</pre>

## Properties

#### EndpointSubsets

_Required_: No

_Type_: List of <a href="endpointsubsetsdefinition.md">EndpointSubsetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cluster

_Required_: No

_Type_: List of <a href="clusterdefinition.md">ClusterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pool

_Required_: No

_Type_: List of <a href="pooldefinition.md">PoolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

