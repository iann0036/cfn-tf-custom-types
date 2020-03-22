# Terraform::OCI::CoreAppCatalogSubscription

This resource provides the App Catalog Subscription resource in Oracle Cloud Infrastructure Core service.

Create a subscription for listing resource version for a compartment. It will take some time to propagate to all regions.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::CoreAppCatalogSubscription",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#eulalink" title="EulaLink">EulaLink</a>" : <i>String</i>,
        "<a href="#listingid" title="ListingId">ListingId</a>" : <i>String</i>,
        "<a href="#listingresourceversion" title="ListingResourceVersion">ListingResourceVersion</a>" : <i>String</i>,
        "<a href="#oracletermsofuselink" title="OracleTermsOfUseLink">OracleTermsOfUseLink</a>" : <i>String</i>,
        "<a href="#signature" title="Signature">Signature</a>" : <i>String</i>,
        "<a href="#timeretrieved" title="TimeRetrieved">TimeRetrieved</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::CoreAppCatalogSubscription
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#eulalink" title="EulaLink">EulaLink</a>: <i>String</i>
    <a href="#listingid" title="ListingId">ListingId</a>: <i>String</i>
    <a href="#listingresourceversion" title="ListingResourceVersion">ListingResourceVersion</a>: <i>String</i>
    <a href="#oracletermsofuselink" title="OracleTermsOfUseLink">OracleTermsOfUseLink</a>: <i>String</i>
    <a href="#signature" title="Signature">Signature</a>: <i>String</i>
    <a href="#timeretrieved" title="TimeRetrieved">TimeRetrieved</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### CompartmentId

The compartmentID for the subscription.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EulaLink

EULA link.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListingId

The OCID of the listing.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListingResourceVersion

Listing resource version.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OracleTermsOfUseLink

Oracle TOU link.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Signature

A generated signature for this listing resource version retrieved the agreements API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeRetrieved

Date and time the agreements were retrieved, in RFC3339 format. Example: `2018-03-20T12:32:53.532Z`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DisplayName

Returns the <code>DisplayName</code> value.

#### Id

Returns the <code>Id</code> value.

#### ListingResourceId

Returns the <code>ListingResourceId</code> value.

#### PublisherName

Returns the <code>PublisherName</code> value.

#### Summary

Returns the <code>Summary</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

