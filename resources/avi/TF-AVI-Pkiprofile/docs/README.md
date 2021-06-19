# TF::AVI::Pkiprofile

The PKIProfile resource allows the creation and management of Avi PKIProfile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Pkiprofile",
    "Properties" : {
        "<a href="#createdby" title="CreatedBy">CreatedBy</a>" : <i>String</i>,
        "<a href="#crlcheck" title="CrlCheck">CrlCheck</a>" : <i>Boolean</i>,
        "<a href="#ignorepeerchain" title="IgnorePeerChain">IgnorePeerChain</a>" : <i>Boolean</i>,
        "<a href="#isfederated" title="IsFederated">IsFederated</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#validateonlyleafcrl" title="ValidateOnlyLeafCrl">ValidateOnlyLeafCrl</a>" : <i>Boolean</i>,
        "<a href="#cacerts" title="CaCerts">CaCerts</a>" : <i>[ <a href="cacertsdefinition.md">CaCertsDefinition</a>, ... ]</i>,
        "<a href="#crls" title="Crls">Crls</a>" : <i>[ <a href="crlsdefinition.md">CrlsDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Pkiprofile
Properties:
    <a href="#createdby" title="CreatedBy">CreatedBy</a>: <i>String</i>
    <a href="#crlcheck" title="CrlCheck">CrlCheck</a>: <i>Boolean</i>
    <a href="#ignorepeerchain" title="IgnorePeerChain">IgnorePeerChain</a>: <i>Boolean</i>
    <a href="#isfederated" title="IsFederated">IsFederated</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#validateonlyleafcrl" title="ValidateOnlyLeafCrl">ValidateOnlyLeafCrl</a>: <i>Boolean</i>
    <a href="#cacerts" title="CaCerts">CaCerts</a>: <i>
      - <a href="cacertsdefinition.md">CaCertsDefinition</a></i>
    <a href="#crls" title="Crls">Crls</a>: <i>
      - <a href="crlsdefinition.md">CrlsDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
</pre>

## Properties

#### CreatedBy

Creator name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrlCheck

When enabled, avi will verify via crl checks that certificates in the trust chain have not been revoked.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnorePeerChain

When enabled, avi will not trust intermediate and root certs presented by a client. Instead, only the chain certs configured in the certificate authority section will be used to verify trust of the client's cert. Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition. Special default for basic edition is true, essentials edition is true, enterprise is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsFederated

This field describes the object's replication scope. If the field is set to false, then the object is visible within the controller-cluster and its associated service-engines. If the field is set to true, then the object is replicated across the federation. Field introduced in 17.1.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the pki profile.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidateOnlyLeafCrl

When enabled, avi will only validate the revocation status of the leaf certificate using crl. To enable validation for the entire chain, disable this option and provide all the relevant crls. Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaCerts

_Required_: No

_Type_: List of <a href="cacertsdefinition.md">CaCertsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Crls

_Required_: No

_Type_: List of <a href="crlsdefinition.md">CrlsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

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

