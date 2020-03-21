# Terraform::AzureRM::VirtualNetworkGateway VpnClientConfiguration RootCertificate

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#publiccertdata" title="PublicCertData">PublicCertData</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#publiccertdata" title="PublicCertData">PublicCertData</a>: <i>String</i>
</pre>

## Properties

#### Name

A user-defined name of the revoked certificate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicCertData

The SHA1 thumbprint of the certificate to be
revoked.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

