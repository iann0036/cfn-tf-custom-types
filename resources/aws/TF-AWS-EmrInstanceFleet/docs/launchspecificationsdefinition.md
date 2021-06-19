# TF::AWS::EmrInstanceFleet LaunchSpecificationsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ondemandspecification" title="OnDemandSpecification">OnDemandSpecification</a>" : <i>[ <a href="ondemandspecificationdefinition.md">OnDemandSpecificationDefinition</a>, ... ]</i>,
    "<a href="#spotspecification" title="SpotSpecification">SpotSpecification</a>" : <i>[ <a href="spotspecificationdefinition.md">SpotSpecificationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ondemandspecification" title="OnDemandSpecification">OnDemandSpecification</a>: <i>
      - <a href="ondemandspecificationdefinition.md">OnDemandSpecificationDefinition</a></i>
<a href="#spotspecification" title="SpotSpecification">SpotSpecification</a>: <i>
      - <a href="spotspecificationdefinition.md">SpotSpecificationDefinition</a></i>
</pre>

## Properties

#### OnDemandSpecification

_Required_: No

_Type_: List of <a href="ondemandspecificationdefinition.md">OnDemandSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotSpecification

_Required_: No

_Type_: List of <a href="spotspecificationdefinition.md">SpotSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

