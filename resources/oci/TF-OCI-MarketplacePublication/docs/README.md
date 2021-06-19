# TF::OCI::MarketplacePublication

This resource provides the Publication resource in Oracle Cloud Infrastructure Marketplace service.

Creates a publication of the given type with an optional default package

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::MarketplacePublication",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#isagreementacknowledged" title="IsAgreementAcknowledged">IsAgreementAcknowledged</a>" : <i>Boolean</i>,
        "<a href="#listingtype" title="ListingType">ListingType</a>" : <i>String</i>,
        "<a href="#longdescription" title="LongDescription">LongDescription</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#shortdescription" title="ShortDescription">ShortDescription</a>" : <i>String</i>,
        "<a href="#packagedetails" title="PackageDetails">PackageDetails</a>" : <i>[ <a href="packagedetailsdefinition.md">PackageDetailsDefinition</a>, ... ]</i>,
        "<a href="#supportcontacts" title="SupportContacts">SupportContacts</a>" : <i>[ <a href="supportcontactsdefinition.md">SupportContactsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::MarketplacePublication
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#isagreementacknowledged" title="IsAgreementAcknowledged">IsAgreementAcknowledged</a>: <i>Boolean</i>
    <a href="#listingtype" title="ListingType">ListingType</a>: <i>String</i>
    <a href="#longdescription" title="LongDescription">LongDescription</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#shortdescription" title="ShortDescription">ShortDescription</a>: <i>String</i>
    <a href="#packagedetails" title="PackageDetails">PackageDetails</a>: <i>
      - <a href="packagedetailsdefinition.md">PackageDetailsDefinition</a></i>
    <a href="#supportcontacts" title="SupportContacts">SupportContacts</a>: <i>
      - <a href="supportcontactsdefinition.md">SupportContactsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CompartmentId

(Updatable) The OCID of the compartment to create the resource within.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAgreementAcknowledged

Acknowledgement that invoker has the right and authority to share this Community Image in accordance with their agreement with Oracle applicable to the Services and the related Service Specifications.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListingType

In which catalog the listing should exist.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LongDescription

(Updatable) short description of the catalog listing.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

(Updatable) The name of the contact.
* `phone` - (Optional) (Updatable) The phone number of the contact.
* `subject` - (Optional) (Updatable) The email subject line to use when contacting support.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShortDescription

(Updatable) short description of the catalog listing.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageDetails

_Required_: No

_Type_: List of <a href="packagedetailsdefinition.md">PackageDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportContacts

_Required_: No

_Type_: List of <a href="supportcontactsdefinition.md">SupportContactsDefinition</a>

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

#### Icon

Returns the <code>Icon</code> value.

#### Id

Returns the <code>Id</code> value.

#### PackageType

Type of the artifact of the listing
* `package_version` - (Required) The version of the package.

#### State

Returns the <code>State</code> value.

#### SupportedOperatingSystems

Returns the <code>SupportedOperatingSystems</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

