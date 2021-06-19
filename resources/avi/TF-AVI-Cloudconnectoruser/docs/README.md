# TF::AVI::Cloudconnectoruser

The CloudConnectorUser resource allows the creation and management of Avi CloudConnectorUser

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Cloudconnectoruser",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>String</i>,
        "<a href="#publickey" title="PublicKey">PublicKey</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#azureserviceprincipal" title="AzureServiceprincipal">AzureServiceprincipal</a>" : <i>[ <a href="azureserviceprincipaldefinition.md">AzureServiceprincipalDefinition</a>, ... ]</i>,
        "<a href="#azureuserpass" title="AzureUserpass">AzureUserpass</a>" : <i>[ <a href="azureuserpassdefinition.md">AzureUserpassDefinition</a>, ... ]</i>,
        "<a href="#gcpcredentials" title="GcpCredentials">GcpCredentials</a>" : <i>[ <a href="gcpcredentialsdefinition.md">GcpCredentialsDefinition</a>, ... ]</i>,
        "<a href="#nsxtcredentials" title="NsxtCredentials">NsxtCredentials</a>" : <i>[ <a href="nsxtcredentialsdefinition.md">NsxtCredentialsDefinition</a>, ... ]</i>,
        "<a href="#ocicredentials" title="OciCredentials">OciCredentials</a>" : <i>[ <a href="ocicredentialsdefinition.md">OciCredentialsDefinition</a>, ... ]</i>,
        "<a href="#tencentcredentials" title="TencentCredentials">TencentCredentials</a>" : <i>[ <a href="tencentcredentialsdefinition.md">TencentCredentialsDefinition</a>, ... ]</i>,
        "<a href="#vcentercredentials" title="VcenterCredentials">VcenterCredentials</a>" : <i>[ <a href="vcentercredentialsdefinition.md">VcenterCredentialsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Cloudconnectoruser
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>String</i>
    <a href="#publickey" title="PublicKey">PublicKey</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#azureserviceprincipal" title="AzureServiceprincipal">AzureServiceprincipal</a>: <i>
      - <a href="azureserviceprincipaldefinition.md">AzureServiceprincipalDefinition</a></i>
    <a href="#azureuserpass" title="AzureUserpass">AzureUserpass</a>: <i>
      - <a href="azureuserpassdefinition.md">AzureUserpassDefinition</a></i>
    <a href="#gcpcredentials" title="GcpCredentials">GcpCredentials</a>: <i>
      - <a href="gcpcredentialsdefinition.md">GcpCredentialsDefinition</a></i>
    <a href="#nsxtcredentials" title="NsxtCredentials">NsxtCredentials</a>: <i>
      - <a href="nsxtcredentialsdefinition.md">NsxtCredentialsDefinition</a></i>
    <a href="#ocicredentials" title="OciCredentials">OciCredentials</a>: <i>
      - <a href="ocicredentialsdefinition.md">OciCredentialsDefinition</a></i>
    <a href="#tencentcredentials" title="TencentCredentials">TencentCredentials</a>: <i>
      - <a href="tencentcredentialsdefinition.md">TencentCredentialsDefinition</a></i>
    <a href="#vcentercredentials" title="VcenterCredentials">VcenterCredentials</a>: <i>
      - <a href="vcentercredentialsdefinition.md">VcenterCredentialsDefinition</a></i>
</pre>

## Properties

#### Name

Name of the object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Placeholder for description of property password of obj type cloudconnectoruser field type string  type str.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

Placeholder for description of property private_key of obj type cloudconnectoruser field type string  type str.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKey

Placeholder for description of property public_key of obj type cloudconnectoruser field type string  type str.

_Required_: No

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

#### AzureServiceprincipal

_Required_: No

_Type_: List of <a href="azureserviceprincipaldefinition.md">AzureServiceprincipalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureUserpass

_Required_: No

_Type_: List of <a href="azureuserpassdefinition.md">AzureUserpassDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpCredentials

_Required_: No

_Type_: List of <a href="gcpcredentialsdefinition.md">GcpCredentialsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxtCredentials

_Required_: No

_Type_: List of <a href="nsxtcredentialsdefinition.md">NsxtCredentialsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OciCredentials

_Required_: No

_Type_: List of <a href="ocicredentialsdefinition.md">OciCredentialsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TencentCredentials

_Required_: No

_Type_: List of <a href="tencentcredentialsdefinition.md">TencentCredentialsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterCredentials

_Required_: No

_Type_: List of <a href="vcentercredentialsdefinition.md">VcenterCredentialsDefinition</a>

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

