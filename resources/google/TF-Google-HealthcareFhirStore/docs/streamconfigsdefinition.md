# TF::Google::HealthcareFhirStore StreamConfigsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#resourcetypes" title="ResourceTypes">ResourceTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#bigquerydestination" title="BigqueryDestination">BigqueryDestination</a>" : <i>[ <a href="bigquerydestinationdefinition.md">BigqueryDestinationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#resourcetypes" title="ResourceTypes">ResourceTypes</a>: <i>
      - String</i>
<a href="#bigquerydestination" title="BigqueryDestination">BigqueryDestination</a>: <i>
      - <a href="bigquerydestinationdefinition.md">BigqueryDestinationDefinition</a></i>
</pre>

## Properties

#### ResourceTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigqueryDestination

_Required_: No

_Type_: List of <a href="bigquerydestinationdefinition.md">BigqueryDestinationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

