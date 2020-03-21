# Terraform::OCI::CoreInstanceConfiguration InstanceDetails LaunchDetails

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
    "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
    "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="instancedetails-launchdetails-definedtags.md">DefinedTags</a>, ... ]</i>,
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#extendedmetadata" title="ExtendedMetadata">ExtendedMetadata</a>" : <i>[ <a href="instancedetails-launchdetails-extendedmetadata.md">ExtendedMetadata</a>, ... ]</i>,
    "<a href="#faultdomain" title="FaultDomain">FaultDomain</a>" : <i>String</i>,
    "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="instancedetails-launchdetails-freeformtags.md">FreeformTags</a>, ... ]</i>,
    "<a href="#ipxescript" title="IpxeScript">IpxeScript</a>" : <i>String</i>,
    "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="instancedetails-launchdetails-metadata.md">Metadata</a>, ... ]</i>,
    "<a href="#shape" title="Shape">Shape</a>" : <i>String</i>,
    "<a href="#createvnicdetails" title="CreateVnicDetails">CreateVnicDetails</a>" : <i>[ <a href="instancedetails-launchdetails-createvnicdetails.md">CreateVnicDetails</a>, ... ]</i>,
    "<a href="#sourcedetails" title="SourceDetails">SourceDetails</a>" : <i>[ <a href="instancedetails-launchdetails-sourcedetails.md">SourceDetails</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
<a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
<a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="instancedetails-launchdetails-definedtags.md">DefinedTags</a></i>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#extendedmetadata" title="ExtendedMetadata">ExtendedMetadata</a>: <i>
      - <a href="instancedetails-launchdetails-extendedmetadata.md">ExtendedMetadata</a></i>
<a href="#faultdomain" title="FaultDomain">FaultDomain</a>: <i>String</i>
<a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="instancedetails-launchdetails-freeformtags.md">FreeformTags</a></i>
<a href="#ipxescript" title="IpxeScript">IpxeScript</a>: <i>String</i>
<a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="instancedetails-launchdetails-metadata.md">Metadata</a></i>
<a href="#shape" title="Shape">Shape</a>: <i>String</i>
<a href="#createvnicdetails" title="CreateVnicDetails">CreateVnicDetails</a>: <i>
      - <a href="instancedetails-launchdetails-createvnicdetails.md">CreateVnicDetails</a></i>
<a href="#sourcedetails" title="SourceDetails">SourceDetails</a>: <i>
      - <a href="instancedetails-launchdetails-sourcedetails.md">SourceDetails</a></i>
</pre>

## Properties

#### AvailabilityDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of <a href="instancedetails-launchdetails-definedtags.md">DefinedTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedMetadata

_Required_: No

_Type_: List of <a href="instancedetails-launchdetails-extendedmetadata.md">ExtendedMetadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaultDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of <a href="instancedetails-launchdetails-freeformtags.md">FreeformTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpxeScript

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="instancedetails-launchdetails-metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateVnicDetails

_Required_: No

_Type_: List of <a href="instancedetails-launchdetails-createvnicdetails.md">CreateVnicDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDetails

_Required_: No

_Type_: List of <a href="instancedetails-launchdetails-sourcedetails.md">SourceDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

