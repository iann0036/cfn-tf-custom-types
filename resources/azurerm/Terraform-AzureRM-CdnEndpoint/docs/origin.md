# Terraform::AzureRM::CdnEndpoint Origin

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hostname" title="HostName">HostName</a>" : <i>String</i>,
    "<a href="#httpport" title="HttpPort">HttpPort</a>" : <i>Double</i>,
    "<a href="#httpsport" title="HttpsPort">HttpsPort</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#hostname" title="HostName">HostName</a>: <i>String</i>
<a href="#httpport" title="HttpPort">HttpPort</a>: <i>Double</i>
<a href="#httpsport" title="HttpsPort">HttpsPort</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### HostName

A string that determines the hostname/IP address of the origin server. This string can be a domain name, Storage Account endpoint, Web App endpoint, IPv4 address or IPv6 address. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpPort

The HTTP port of the origin. Defaults to `80`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsPort

The HTTPS port of the origin. Defaults to `443`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the origin. This is an arbitrary value. However, this value needs to be unique under the endpoint. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

