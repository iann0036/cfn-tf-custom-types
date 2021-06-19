# TF::ECL::VnaApplianceV1

Manages a V1 Virtual Network Appliance resource within Enterprise Cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ECL::VnaApplianceV1",
    "Properties" : {
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#defaultgateway" title="DefaultGateway">DefaultGateway</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#interface1noallowedaddresspairs" title="Interface1NoAllowedAddressPairs">Interface1NoAllowedAddressPairs</a>" : <i>Boolean</i>,
        "<a href="#interface1nofixedips" title="Interface1NoFixedIps">Interface1NoFixedIps</a>" : <i>Boolean</i>,
        "<a href="#interface2noallowedaddresspairs" title="Interface2NoAllowedAddressPairs">Interface2NoAllowedAddressPairs</a>" : <i>Boolean</i>,
        "<a href="#interface2nofixedips" title="Interface2NoFixedIps">Interface2NoFixedIps</a>" : <i>Boolean</i>,
        "<a href="#interface3noallowedaddresspairs" title="Interface3NoAllowedAddressPairs">Interface3NoAllowedAddressPairs</a>" : <i>Boolean</i>,
        "<a href="#interface3nofixedips" title="Interface3NoFixedIps">Interface3NoFixedIps</a>" : <i>Boolean</i>,
        "<a href="#interface4noallowedaddresspairs" title="Interface4NoAllowedAddressPairs">Interface4NoAllowedAddressPairs</a>" : <i>Boolean</i>,
        "<a href="#interface4nofixedips" title="Interface4NoFixedIps">Interface4NoFixedIps</a>" : <i>Boolean</i>,
        "<a href="#interface5noallowedaddresspairs" title="Interface5NoAllowedAddressPairs">Interface5NoAllowedAddressPairs</a>" : <i>Boolean</i>,
        "<a href="#interface5nofixedips" title="Interface5NoFixedIps">Interface5NoFixedIps</a>" : <i>Boolean</i>,
        "<a href="#interface6noallowedaddresspairs" title="Interface6NoAllowedAddressPairs">Interface6NoAllowedAddressPairs</a>" : <i>Boolean</i>,
        "<a href="#interface6nofixedips" title="Interface6NoFixedIps">Interface6NoFixedIps</a>" : <i>Boolean</i>,
        "<a href="#interface7noallowedaddresspairs" title="Interface7NoAllowedAddressPairs">Interface7NoAllowedAddressPairs</a>" : <i>Boolean</i>,
        "<a href="#interface7nofixedips" title="Interface7NoFixedIps">Interface7NoFixedIps</a>" : <i>Boolean</i>,
        "<a href="#interface8noallowedaddresspairs" title="Interface8NoAllowedAddressPairs">Interface8NoAllowedAddressPairs</a>" : <i>Boolean</i>,
        "<a href="#interface8nofixedips" title="Interface8NoFixedIps">Interface8NoFixedIps</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#virtualnetworkapplianceplanid" title="VirtualNetworkAppliancePlanId">VirtualNetworkAppliancePlanId</a>" : <i>String</i>,
        "<a href="#interface1allowedaddresspairs" title="Interface1AllowedAddressPairs">Interface1AllowedAddressPairs</a>" : <i>[ <a href="interface1allowedaddresspairsdefinition.md">Interface1AllowedAddressPairsDefinition</a>, ... ]</i>,
        "<a href="#interface1fixedips" title="Interface1FixedIps">Interface1FixedIps</a>" : <i>[ <a href="interface1fixedipsdefinition.md">Interface1FixedIpsDefinition</a>, ... ]</i>,
        "<a href="#interface1info" title="Interface1Info">Interface1Info</a>" : <i>[ <a href="interface1infodefinition.md">Interface1InfoDefinition</a>, ... ]</i>,
        "<a href="#interface2allowedaddresspairs" title="Interface2AllowedAddressPairs">Interface2AllowedAddressPairs</a>" : <i>[ <a href="interface2allowedaddresspairsdefinition.md">Interface2AllowedAddressPairsDefinition</a>, ... ]</i>,
        "<a href="#interface2fixedips" title="Interface2FixedIps">Interface2FixedIps</a>" : <i>[ <a href="interface2fixedipsdefinition.md">Interface2FixedIpsDefinition</a>, ... ]</i>,
        "<a href="#interface2info" title="Interface2Info">Interface2Info</a>" : <i>[ <a href="interface2infodefinition.md">Interface2InfoDefinition</a>, ... ]</i>,
        "<a href="#interface3allowedaddresspairs" title="Interface3AllowedAddressPairs">Interface3AllowedAddressPairs</a>" : <i>[ <a href="interface3allowedaddresspairsdefinition.md">Interface3AllowedAddressPairsDefinition</a>, ... ]</i>,
        "<a href="#interface3fixedips" title="Interface3FixedIps">Interface3FixedIps</a>" : <i>[ <a href="interface3fixedipsdefinition.md">Interface3FixedIpsDefinition</a>, ... ]</i>,
        "<a href="#interface3info" title="Interface3Info">Interface3Info</a>" : <i>[ <a href="interface3infodefinition.md">Interface3InfoDefinition</a>, ... ]</i>,
        "<a href="#interface4allowedaddresspairs" title="Interface4AllowedAddressPairs">Interface4AllowedAddressPairs</a>" : <i>[ <a href="interface4allowedaddresspairsdefinition.md">Interface4AllowedAddressPairsDefinition</a>, ... ]</i>,
        "<a href="#interface4fixedips" title="Interface4FixedIps">Interface4FixedIps</a>" : <i>[ <a href="interface4fixedipsdefinition.md">Interface4FixedIpsDefinition</a>, ... ]</i>,
        "<a href="#interface4info" title="Interface4Info">Interface4Info</a>" : <i>[ <a href="interface4infodefinition.md">Interface4InfoDefinition</a>, ... ]</i>,
        "<a href="#interface5allowedaddresspairs" title="Interface5AllowedAddressPairs">Interface5AllowedAddressPairs</a>" : <i>[ <a href="interface5allowedaddresspairsdefinition.md">Interface5AllowedAddressPairsDefinition</a>, ... ]</i>,
        "<a href="#interface5fixedips" title="Interface5FixedIps">Interface5FixedIps</a>" : <i>[ <a href="interface5fixedipsdefinition.md">Interface5FixedIpsDefinition</a>, ... ]</i>,
        "<a href="#interface5info" title="Interface5Info">Interface5Info</a>" : <i>[ <a href="interface5infodefinition.md">Interface5InfoDefinition</a>, ... ]</i>,
        "<a href="#interface6allowedaddresspairs" title="Interface6AllowedAddressPairs">Interface6AllowedAddressPairs</a>" : <i>[ <a href="interface6allowedaddresspairsdefinition.md">Interface6AllowedAddressPairsDefinition</a>, ... ]</i>,
        "<a href="#interface6fixedips" title="Interface6FixedIps">Interface6FixedIps</a>" : <i>[ <a href="interface6fixedipsdefinition.md">Interface6FixedIpsDefinition</a>, ... ]</i>,
        "<a href="#interface6info" title="Interface6Info">Interface6Info</a>" : <i>[ <a href="interface6infodefinition.md">Interface6InfoDefinition</a>, ... ]</i>,
        "<a href="#interface7allowedaddresspairs" title="Interface7AllowedAddressPairs">Interface7AllowedAddressPairs</a>" : <i>[ <a href="interface7allowedaddresspairsdefinition.md">Interface7AllowedAddressPairsDefinition</a>, ... ]</i>,
        "<a href="#interface7fixedips" title="Interface7FixedIps">Interface7FixedIps</a>" : <i>[ <a href="interface7fixedipsdefinition.md">Interface7FixedIpsDefinition</a>, ... ]</i>,
        "<a href="#interface7info" title="Interface7Info">Interface7Info</a>" : <i>[ <a href="interface7infodefinition.md">Interface7InfoDefinition</a>, ... ]</i>,
        "<a href="#interface8allowedaddresspairs" title="Interface8AllowedAddressPairs">Interface8AllowedAddressPairs</a>" : <i>[ <a href="interface8allowedaddresspairsdefinition.md">Interface8AllowedAddressPairsDefinition</a>, ... ]</i>,
        "<a href="#interface8fixedips" title="Interface8FixedIps">Interface8FixedIps</a>" : <i>[ <a href="interface8fixedipsdefinition.md">Interface8FixedIpsDefinition</a>, ... ]</i>,
        "<a href="#interface8info" title="Interface8Info">Interface8Info</a>" : <i>[ <a href="interface8infodefinition.md">Interface8InfoDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ECL::VnaApplianceV1
Properties:
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#defaultgateway" title="DefaultGateway">DefaultGateway</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#interface1noallowedaddresspairs" title="Interface1NoAllowedAddressPairs">Interface1NoAllowedAddressPairs</a>: <i>Boolean</i>
    <a href="#interface1nofixedips" title="Interface1NoFixedIps">Interface1NoFixedIps</a>: <i>Boolean</i>
    <a href="#interface2noallowedaddresspairs" title="Interface2NoAllowedAddressPairs">Interface2NoAllowedAddressPairs</a>: <i>Boolean</i>
    <a href="#interface2nofixedips" title="Interface2NoFixedIps">Interface2NoFixedIps</a>: <i>Boolean</i>
    <a href="#interface3noallowedaddresspairs" title="Interface3NoAllowedAddressPairs">Interface3NoAllowedAddressPairs</a>: <i>Boolean</i>
    <a href="#interface3nofixedips" title="Interface3NoFixedIps">Interface3NoFixedIps</a>: <i>Boolean</i>
    <a href="#interface4noallowedaddresspairs" title="Interface4NoAllowedAddressPairs">Interface4NoAllowedAddressPairs</a>: <i>Boolean</i>
    <a href="#interface4nofixedips" title="Interface4NoFixedIps">Interface4NoFixedIps</a>: <i>Boolean</i>
    <a href="#interface5noallowedaddresspairs" title="Interface5NoAllowedAddressPairs">Interface5NoAllowedAddressPairs</a>: <i>Boolean</i>
    <a href="#interface5nofixedips" title="Interface5NoFixedIps">Interface5NoFixedIps</a>: <i>Boolean</i>
    <a href="#interface6noallowedaddresspairs" title="Interface6NoAllowedAddressPairs">Interface6NoAllowedAddressPairs</a>: <i>Boolean</i>
    <a href="#interface6nofixedips" title="Interface6NoFixedIps">Interface6NoFixedIps</a>: <i>Boolean</i>
    <a href="#interface7noallowedaddresspairs" title="Interface7NoAllowedAddressPairs">Interface7NoAllowedAddressPairs</a>: <i>Boolean</i>
    <a href="#interface7nofixedips" title="Interface7NoFixedIps">Interface7NoFixedIps</a>: <i>Boolean</i>
    <a href="#interface8noallowedaddresspairs" title="Interface8NoAllowedAddressPairs">Interface8NoAllowedAddressPairs</a>: <i>Boolean</i>
    <a href="#interface8nofixedips" title="Interface8NoFixedIps">Interface8NoFixedIps</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#virtualnetworkapplianceplanid" title="VirtualNetworkAppliancePlanId">VirtualNetworkAppliancePlanId</a>: <i>String</i>
    <a href="#interface1allowedaddresspairs" title="Interface1AllowedAddressPairs">Interface1AllowedAddressPairs</a>: <i>
      - <a href="interface1allowedaddresspairsdefinition.md">Interface1AllowedAddressPairsDefinition</a></i>
    <a href="#interface1fixedips" title="Interface1FixedIps">Interface1FixedIps</a>: <i>
      - <a href="interface1fixedipsdefinition.md">Interface1FixedIpsDefinition</a></i>
    <a href="#interface1info" title="Interface1Info">Interface1Info</a>: <i>
      - <a href="interface1infodefinition.md">Interface1InfoDefinition</a></i>
    <a href="#interface2allowedaddresspairs" title="Interface2AllowedAddressPairs">Interface2AllowedAddressPairs</a>: <i>
      - <a href="interface2allowedaddresspairsdefinition.md">Interface2AllowedAddressPairsDefinition</a></i>
    <a href="#interface2fixedips" title="Interface2FixedIps">Interface2FixedIps</a>: <i>
      - <a href="interface2fixedipsdefinition.md">Interface2FixedIpsDefinition</a></i>
    <a href="#interface2info" title="Interface2Info">Interface2Info</a>: <i>
      - <a href="interface2infodefinition.md">Interface2InfoDefinition</a></i>
    <a href="#interface3allowedaddresspairs" title="Interface3AllowedAddressPairs">Interface3AllowedAddressPairs</a>: <i>
      - <a href="interface3allowedaddresspairsdefinition.md">Interface3AllowedAddressPairsDefinition</a></i>
    <a href="#interface3fixedips" title="Interface3FixedIps">Interface3FixedIps</a>: <i>
      - <a href="interface3fixedipsdefinition.md">Interface3FixedIpsDefinition</a></i>
    <a href="#interface3info" title="Interface3Info">Interface3Info</a>: <i>
      - <a href="interface3infodefinition.md">Interface3InfoDefinition</a></i>
    <a href="#interface4allowedaddresspairs" title="Interface4AllowedAddressPairs">Interface4AllowedAddressPairs</a>: <i>
      - <a href="interface4allowedaddresspairsdefinition.md">Interface4AllowedAddressPairsDefinition</a></i>
    <a href="#interface4fixedips" title="Interface4FixedIps">Interface4FixedIps</a>: <i>
      - <a href="interface4fixedipsdefinition.md">Interface4FixedIpsDefinition</a></i>
    <a href="#interface4info" title="Interface4Info">Interface4Info</a>: <i>
      - <a href="interface4infodefinition.md">Interface4InfoDefinition</a></i>
    <a href="#interface5allowedaddresspairs" title="Interface5AllowedAddressPairs">Interface5AllowedAddressPairs</a>: <i>
      - <a href="interface5allowedaddresspairsdefinition.md">Interface5AllowedAddressPairsDefinition</a></i>
    <a href="#interface5fixedips" title="Interface5FixedIps">Interface5FixedIps</a>: <i>
      - <a href="interface5fixedipsdefinition.md">Interface5FixedIpsDefinition</a></i>
    <a href="#interface5info" title="Interface5Info">Interface5Info</a>: <i>
      - <a href="interface5infodefinition.md">Interface5InfoDefinition</a></i>
    <a href="#interface6allowedaddresspairs" title="Interface6AllowedAddressPairs">Interface6AllowedAddressPairs</a>: <i>
      - <a href="interface6allowedaddresspairsdefinition.md">Interface6AllowedAddressPairsDefinition</a></i>
    <a href="#interface6fixedips" title="Interface6FixedIps">Interface6FixedIps</a>: <i>
      - <a href="interface6fixedipsdefinition.md">Interface6FixedIpsDefinition</a></i>
    <a href="#interface6info" title="Interface6Info">Interface6Info</a>: <i>
      - <a href="interface6infodefinition.md">Interface6InfoDefinition</a></i>
    <a href="#interface7allowedaddresspairs" title="Interface7AllowedAddressPairs">Interface7AllowedAddressPairs</a>: <i>
      - <a href="interface7allowedaddresspairsdefinition.md">Interface7AllowedAddressPairsDefinition</a></i>
    <a href="#interface7fixedips" title="Interface7FixedIps">Interface7FixedIps</a>: <i>
      - <a href="interface7fixedipsdefinition.md">Interface7FixedIpsDefinition</a></i>
    <a href="#interface7info" title="Interface7Info">Interface7Info</a>: <i>
      - <a href="interface7infodefinition.md">Interface7InfoDefinition</a></i>
    <a href="#interface8allowedaddresspairs" title="Interface8AllowedAddressPairs">Interface8AllowedAddressPairs</a>: <i>
      - <a href="interface8allowedaddresspairsdefinition.md">Interface8AllowedAddressPairsDefinition</a></i>
    <a href="#interface8fixedips" title="Interface8FixedIps">Interface8FixedIps</a>: <i>
      - <a href="interface8fixedipsdefinition.md">Interface8FixedIpsDefinition</a></i>
    <a href="#interface8info" title="Interface8Info">Interface8Info</a>: <i>
      - <a href="interface8infodefinition.md">Interface8InfoDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AvailabilityZone

Availability Zone,
this can be referred to using Virtual Server (Nova)'s
list availability zones.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultGateway

IP address of default gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the Virtual Network Appliance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface1NoAllowedAddressPairs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface1NoFixedIps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface2NoAllowedAddressPairs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface2NoFixedIps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface3NoAllowedAddressPairs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface3NoFixedIps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface4NoAllowedAddressPairs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface4NoFixedIps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface5NoAllowedAddressPairs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface5NoFixedIps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface6NoAllowedAddressPairs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface6NoFixedIps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface7NoAllowedAddressPairs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface7NoFixedIps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface8NoAllowedAddressPairs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface8NoFixedIps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the Virtual Network Appliance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Tags of the Virtual Network Appliance.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

Tenant ID of the owner (UUID).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkAppliancePlanId

ID of the Virtual Network Appliance Plan.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface1AllowedAddressPairs

_Required_: No

_Type_: List of <a href="interface1allowedaddresspairsdefinition.md">Interface1AllowedAddressPairsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface1FixedIps

_Required_: No

_Type_: List of <a href="interface1fixedipsdefinition.md">Interface1FixedIpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface1Info

_Required_: No

_Type_: List of <a href="interface1infodefinition.md">Interface1InfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface2AllowedAddressPairs

_Required_: No

_Type_: List of <a href="interface2allowedaddresspairsdefinition.md">Interface2AllowedAddressPairsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface2FixedIps

_Required_: No

_Type_: List of <a href="interface2fixedipsdefinition.md">Interface2FixedIpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface2Info

_Required_: No

_Type_: List of <a href="interface2infodefinition.md">Interface2InfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface3AllowedAddressPairs

_Required_: No

_Type_: List of <a href="interface3allowedaddresspairsdefinition.md">Interface3AllowedAddressPairsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface3FixedIps

_Required_: No

_Type_: List of <a href="interface3fixedipsdefinition.md">Interface3FixedIpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface3Info

_Required_: No

_Type_: List of <a href="interface3infodefinition.md">Interface3InfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface4AllowedAddressPairs

_Required_: No

_Type_: List of <a href="interface4allowedaddresspairsdefinition.md">Interface4AllowedAddressPairsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface4FixedIps

_Required_: No

_Type_: List of <a href="interface4fixedipsdefinition.md">Interface4FixedIpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface4Info

_Required_: No

_Type_: List of <a href="interface4infodefinition.md">Interface4InfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface5AllowedAddressPairs

_Required_: No

_Type_: List of <a href="interface5allowedaddresspairsdefinition.md">Interface5AllowedAddressPairsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface5FixedIps

_Required_: No

_Type_: List of <a href="interface5fixedipsdefinition.md">Interface5FixedIpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface5Info

_Required_: No

_Type_: List of <a href="interface5infodefinition.md">Interface5InfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface6AllowedAddressPairs

_Required_: No

_Type_: List of <a href="interface6allowedaddresspairsdefinition.md">Interface6AllowedAddressPairsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface6FixedIps

_Required_: No

_Type_: List of <a href="interface6fixedipsdefinition.md">Interface6FixedIpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface6Info

_Required_: No

_Type_: List of <a href="interface6infodefinition.md">Interface6InfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface7AllowedAddressPairs

_Required_: No

_Type_: List of <a href="interface7allowedaddresspairsdefinition.md">Interface7AllowedAddressPairsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface7FixedIps

_Required_: No

_Type_: List of <a href="interface7fixedipsdefinition.md">Interface7FixedIpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface7Info

_Required_: No

_Type_: List of <a href="interface7infodefinition.md">Interface7InfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface8AllowedAddressPairs

_Required_: No

_Type_: List of <a href="interface8allowedaddresspairsdefinition.md">Interface8AllowedAddressPairsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface8FixedIps

_Required_: No

_Type_: List of <a href="interface8fixedipsdefinition.md">Interface8FixedIpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface8Info

_Required_: No

_Type_: List of <a href="interface8infodefinition.md">Interface8InfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

