# TF::Dynatrace::CalculatedServiceMetric SourceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#managementzone" title="ManagementZone">ManagementZone</a>" : <i>String</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#servicetag" title="ServiceTag">ServiceTag</a>" : <i>[ <a href="servicetagdefinition.md">ServiceTagDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#managementzone" title="ManagementZone">ManagementZone</a>: <i>String</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#servicetag" title="ServiceTag">ServiceTag</a>: <i>
      - <a href="servicetagdefinition.md">ServiceTagDefinition</a></i>
</pre>

## Properties

#### ManagementZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceTag

_Required_: No

_Type_: List of <a href="servicetagdefinition.md">ServiceTagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

