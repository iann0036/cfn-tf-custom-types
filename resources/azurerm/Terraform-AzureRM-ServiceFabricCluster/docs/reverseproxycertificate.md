# Terraform::AzureRM::ServiceFabricCluster ReverseProxyCertificate

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#thumbprint" title="Thumbprint">Thumbprint</a>" : <i>String</i>,
    "<a href="#thumbprintsecondary" title="ThumbprintSecondary">ThumbprintSecondary</a>" : <i>String</i>,
    "<a href="#x509storename" title="X509StoreName">X509StoreName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#thumbprint" title="Thumbprint">Thumbprint</a>: <i>String</i>
<a href="#thumbprintsecondary" title="ThumbprintSecondary">ThumbprintSecondary</a>: <i>String</i>
<a href="#x509storename" title="X509StoreName">X509StoreName</a>: <i>String</i>
</pre>

## Properties

#### Thumbprint

The Thumbprint of the Certificate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThumbprintSecondary

The Secondary Thumbprint of the Certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### X509StoreName

The X509 Store where the Certificate Exists, such as `My`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

