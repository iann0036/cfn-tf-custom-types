# TF::RedisCloud::Subscription RegionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#multipleavailabilityzones" title="MultipleAvailabilityZones">MultipleAvailabilityZones</a>" : <i>Boolean</i>,
    "<a href="#networkingdeploymentcidr" title="NetworkingDeploymentCidr">NetworkingDeploymentCidr</a>" : <i>String</i>,
    "<a href="#networkingvpcid" title="NetworkingVpcId">NetworkingVpcId</a>" : <i>String</i>,
    "<a href="#preferredavailabilityzones" title="PreferredAvailabilityZones">PreferredAvailabilityZones</a>" : <i>[ String, ... ]</i>,
    "<a href="#region" title="Region">Region</a>" : <i>[ <a href="regiondefinition.md">RegionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#multipleavailabilityzones" title="MultipleAvailabilityZones">MultipleAvailabilityZones</a>: <i>Boolean</i>
<a href="#networkingdeploymentcidr" title="NetworkingDeploymentCidr">NetworkingDeploymentCidr</a>: <i>String</i>
<a href="#networkingvpcid" title="NetworkingVpcId">NetworkingVpcId</a>: <i>String</i>
<a href="#preferredavailabilityzones" title="PreferredAvailabilityZones">PreferredAvailabilityZones</a>: <i>
      - String</i>
<a href="#region" title="Region">Region</a>: <i>
      - <a href="regiondefinition.md">RegionDefinition</a></i>
</pre>

## Properties

#### MultipleAvailabilityZones

Support deployment on multiple availability zones within the selected region. Default: ‘false’.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkingDeploymentCidr

Deployment CIDR mask.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkingVpcId

Either an existing VPC Id (already exists in the specific region) or create a new VPC
(if no VPC is specified). VPC Identifier must be in a valid format (for example: ‘vpc-0125be68a4625884ad’) and existing
within the hosting account.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredAvailabilityZones

Availability zones deployment preferences (for the selected provider & region).

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: List of <a href="regiondefinition.md">RegionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

