# TF::Google::ContainerCluster ResourceUsageExportConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enablenetworkegressmetering" title="EnableNetworkEgressMetering">EnableNetworkEgressMetering</a>" : <i>Boolean</i>,
    "<a href="#enableresourceconsumptionmetering" title="EnableResourceConsumptionMetering">EnableResourceConsumptionMetering</a>" : <i>Boolean</i>,
    "<a href="#bigquerydestination" title="BigqueryDestination">BigqueryDestination</a>" : <i>[ <a href="bigquerydestinationdefinition.md">BigqueryDestinationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enablenetworkegressmetering" title="EnableNetworkEgressMetering">EnableNetworkEgressMetering</a>: <i>Boolean</i>
<a href="#enableresourceconsumptionmetering" title="EnableResourceConsumptionMetering">EnableResourceConsumptionMetering</a>: <i>Boolean</i>
<a href="#bigquerydestination" title="BigqueryDestination">BigqueryDestination</a>: <i>
      - <a href="bigquerydestinationdefinition.md">BigqueryDestinationDefinition</a></i>
</pre>

## Properties

#### EnableNetworkEgressMetering

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableResourceConsumptionMetering

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigqueryDestination

_Required_: No

_Type_: List of <a href="bigquerydestinationdefinition.md">BigqueryDestinationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

