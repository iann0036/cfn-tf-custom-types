# TF::Aviatrix::SamlEndpoint

The **aviatrix_saml_endpoint** resource allows the creation and management of [Aviatrix SAML endpoints](https://docs.aviatrix.com/HowTos/VPN_SAML.html).

For details on Aviatrix Controller Login with SAML authentication, please see documentation [here](https://docs.aviatrix.com/HowTos/Controller_Login_SAML_Config.html). This feature is now supported as of Aviatrix Terraform provider release R2.14.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::SamlEndpoint",
    "Properties" : {
        "<a href="#accesssetby" title="AccessSetBy">AccessSetBy</a>" : <i>String</i>,
        "<a href="#controllerlogin" title="ControllerLogin">ControllerLogin</a>" : <i>Boolean</i>,
        "<a href="#customentityid" title="CustomEntityId">CustomEntityId</a>" : <i>String</i>,
        "<a href="#customsamlrequesttemplate" title="CustomSamlRequestTemplate">CustomSamlRequestTemplate</a>" : <i>String</i>,
        "<a href="#endpointname" title="EndpointName">EndpointName</a>" : <i>String</i>,
        "<a href="#idpmetadata" title="IdpMetadata">IdpMetadata</a>" : <i>String</i>,
        "<a href="#idpmetadatatype" title="IdpMetadataType">IdpMetadataType</a>" : <i>String</i>,
        "<a href="#idpmetadataurl" title="IdpMetadataUrl">IdpMetadataUrl</a>" : <i>String</i>,
        "<a href="#rbacgroups" title="RbacGroups">RbacGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#signauthnrequests" title="SignAuthnRequests">SignAuthnRequests</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::SamlEndpoint
Properties:
    <a href="#accesssetby" title="AccessSetBy">AccessSetBy</a>: <i>String</i>
    <a href="#controllerlogin" title="ControllerLogin">ControllerLogin</a>: <i>Boolean</i>
    <a href="#customentityid" title="CustomEntityId">CustomEntityId</a>: <i>String</i>
    <a href="#customsamlrequesttemplate" title="CustomSamlRequestTemplate">CustomSamlRequestTemplate</a>: <i>String</i>
    <a href="#endpointname" title="EndpointName">EndpointName</a>: <i>String</i>
    <a href="#idpmetadata" title="IdpMetadata">IdpMetadata</a>: <i>String</i>
    <a href="#idpmetadatatype" title="IdpMetadataType">IdpMetadataType</a>: <i>String</i>
    <a href="#idpmetadataurl" title="IdpMetadataUrl">IdpMetadataUrl</a>: <i>String</i>
    <a href="#rbacgroups" title="RbacGroups">RbacGroups</a>: <i>
      - String</i>
    <a href="#signauthnrequests" title="SignAuthnRequests">SignAuthnRequests</a>: <i>Boolean</i>
</pre>

## Properties

#### AccessSetBy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerLogin

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomEntityId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomSamlRequestTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpMetadata

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpMetadataType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpMetadataUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RbacGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignAuthnRequests

_Required_: No

_Type_: Boolean

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

