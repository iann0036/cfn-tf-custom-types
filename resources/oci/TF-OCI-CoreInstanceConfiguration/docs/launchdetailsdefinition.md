# TF::OCI::CoreInstanceConfiguration LaunchDetailsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
    "<a href="#capacityreservationid" title="CapacityReservationId">CapacityReservationId</a>" : <i>String</i>,
    "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
    "<a href="#dedicatedvmhostid" title="DedicatedVmHostId">DedicatedVmHostId</a>" : <i>String</i>,
    "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#extendedmetadata" title="ExtendedMetadata">ExtendedMetadata</a>" : <i>[ <a href="extendedmetadatadefinition.md">ExtendedMetadataDefinition</a>, ... ]</i>,
    "<a href="#faultdomain" title="FaultDomain">FaultDomain</a>" : <i>String</i>,
    "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
    "<a href="#ipxescript" title="IpxeScript">IpxeScript</a>" : <i>String</i>,
    "<a href="#ispvencryptionintransitenabled" title="IsPvEncryptionInTransitEnabled">IsPvEncryptionInTransitEnabled</a>" : <i>Boolean</i>,
    "<a href="#launchmode" title="LaunchMode">LaunchMode</a>" : <i>String</i>,
    "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
    "<a href="#preferredmaintenanceaction" title="PreferredMaintenanceAction">PreferredMaintenanceAction</a>" : <i>String</i>,
    "<a href="#shape" title="Shape">Shape</a>" : <i>String</i>,
    "<a href="#agentconfig" title="AgentConfig">AgentConfig</a>" : <i>[ <a href="agentconfigdefinition.md">AgentConfigDefinition</a>, ... ]</i>,
    "<a href="#availabilityconfig" title="AvailabilityConfig">AvailabilityConfig</a>" : <i>[ <a href="availabilityconfigdefinition.md">AvailabilityConfigDefinition</a>, ... ]</i>,
    "<a href="#createvnicdetails" title="CreateVnicDetails">CreateVnicDetails</a>" : <i>[ <a href="createvnicdetailsdefinition.md">CreateVnicDetailsDefinition</a>, ... ]</i>,
    "<a href="#instanceoptions" title="InstanceOptions">InstanceOptions</a>" : <i>[ <a href="instanceoptionsdefinition.md">InstanceOptionsDefinition</a>, ... ]</i>,
    "<a href="#launchoptions" title="LaunchOptions">LaunchOptions</a>" : <i>[ <a href="launchoptionsdefinition.md">LaunchOptionsDefinition</a>, ... ]</i>,
    "<a href="#platformconfig" title="PlatformConfig">PlatformConfig</a>" : <i>[ <a href="platformconfigdefinition.md">PlatformConfigDefinition</a>, ... ]</i>,
    "<a href="#preemptibleinstanceconfig" title="PreemptibleInstanceConfig">PreemptibleInstanceConfig</a>" : <i>[ <a href="preemptibleinstanceconfigdefinition.md">PreemptibleInstanceConfigDefinition</a>, ... ]</i>,
    "<a href="#shapeconfig" title="ShapeConfig">ShapeConfig</a>" : <i>[ <a href="shapeconfigdefinition.md">ShapeConfigDefinition</a>, ... ]</i>,
    "<a href="#sourcedetails" title="SourceDetails">SourceDetails</a>" : <i>[ <a href="sourcedetailsdefinition.md">SourceDetailsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
<a href="#capacityreservationid" title="CapacityReservationId">CapacityReservationId</a>: <i>String</i>
<a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
<a href="#dedicatedvmhostid" title="DedicatedVmHostId">DedicatedVmHostId</a>: <i>String</i>
<a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#extendedmetadata" title="ExtendedMetadata">ExtendedMetadata</a>: <i>
      - <a href="extendedmetadatadefinition.md">ExtendedMetadataDefinition</a></i>
<a href="#faultdomain" title="FaultDomain">FaultDomain</a>: <i>String</i>
<a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
<a href="#ipxescript" title="IpxeScript">IpxeScript</a>: <i>String</i>
<a href="#ispvencryptionintransitenabled" title="IsPvEncryptionInTransitEnabled">IsPvEncryptionInTransitEnabled</a>: <i>Boolean</i>
<a href="#launchmode" title="LaunchMode">LaunchMode</a>: <i>String</i>
<a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
<a href="#preferredmaintenanceaction" title="PreferredMaintenanceAction">PreferredMaintenanceAction</a>: <i>String</i>
<a href="#shape" title="Shape">Shape</a>: <i>String</i>
<a href="#agentconfig" title="AgentConfig">AgentConfig</a>: <i>
      - <a href="agentconfigdefinition.md">AgentConfigDefinition</a></i>
<a href="#availabilityconfig" title="AvailabilityConfig">AvailabilityConfig</a>: <i>
      - <a href="availabilityconfigdefinition.md">AvailabilityConfigDefinition</a></i>
<a href="#createvnicdetails" title="CreateVnicDetails">CreateVnicDetails</a>: <i>
      - <a href="createvnicdetailsdefinition.md">CreateVnicDetailsDefinition</a></i>
<a href="#instanceoptions" title="InstanceOptions">InstanceOptions</a>: <i>
      - <a href="instanceoptionsdefinition.md">InstanceOptionsDefinition</a></i>
<a href="#launchoptions" title="LaunchOptions">LaunchOptions</a>: <i>
      - <a href="launchoptionsdefinition.md">LaunchOptionsDefinition</a></i>
<a href="#platformconfig" title="PlatformConfig">PlatformConfig</a>: <i>
      - <a href="platformconfigdefinition.md">PlatformConfigDefinition</a></i>
<a href="#preemptibleinstanceconfig" title="PreemptibleInstanceConfig">PreemptibleInstanceConfig</a>: <i>
      - <a href="preemptibleinstanceconfigdefinition.md">PreemptibleInstanceConfigDefinition</a></i>
<a href="#shapeconfig" title="ShapeConfig">ShapeConfig</a>: <i>
      - <a href="shapeconfigdefinition.md">ShapeConfigDefinition</a></i>
<a href="#sourcedetails" title="SourceDetails">SourceDetails</a>: <i>
      - <a href="sourcedetailsdefinition.md">SourceDetailsDefinition</a></i>
</pre>

## Properties

#### AvailabilityDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityReservationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DedicatedVmHostId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedMetadata

_Required_: No

_Type_: List of <a href="extendedmetadatadefinition.md">ExtendedMetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaultDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpxeScript

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPvEncryptionInTransitEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredMaintenanceAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AgentConfig

_Required_: No

_Type_: List of <a href="agentconfigdefinition.md">AgentConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityConfig

_Required_: No

_Type_: List of <a href="availabilityconfigdefinition.md">AvailabilityConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateVnicDetails

_Required_: No

_Type_: List of <a href="createvnicdetailsdefinition.md">CreateVnicDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceOptions

_Required_: No

_Type_: List of <a href="instanceoptionsdefinition.md">InstanceOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchOptions

_Required_: No

_Type_: List of <a href="launchoptionsdefinition.md">LaunchOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformConfig

_Required_: No

_Type_: List of <a href="platformconfigdefinition.md">PlatformConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreemptibleInstanceConfig

_Required_: No

_Type_: List of <a href="preemptibleinstanceconfigdefinition.md">PreemptibleInstanceConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShapeConfig

_Required_: No

_Type_: List of <a href="shapeconfigdefinition.md">ShapeConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDetails

_Required_: No

_Type_: List of <a href="sourcedetailsdefinition.md">SourceDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

