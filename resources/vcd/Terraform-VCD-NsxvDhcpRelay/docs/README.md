# Terraform::VCD::NsxvDhcpRelay

Provides a vCloud Director Edge Gateway DHCP relay configuration resource. The DHCP relay capability
provided by NSX in vCloud Director environment allows to leverage existing DHCP infrastructure from
within vCloud Director environment without any interruption to the IP address management in existing
DHCP infrastructure. DHCP messages are relayed from virtual machines to the designated DHCP servers
in your physical DHCP infrastructure, which allows IP addresses controlled by the NSX software to
continue to be in sync with IP addresses in the rest of your DHCP-controlled environments. 

~> **Note:** This resource is a "singleton". Because DHCP relay settings are just edge gateway
properties - only one resource per Edge Gateway is useful.

Supported in provider *v2.6+*

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::NsxvDhcpRelay",
    "Properties" : {
        "<a href="#domainnames" title="DomainNames">DomainNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#edgegateway" title="EdgeGateway">EdgeGateway</a>" : <i>String</i>,
        "<a href="#ipaddresses" title="IpAddresses">IpAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#ipsets" title="IpSets">IpSets</a>" : <i>[ String, ... ]</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>,
        "<a href="#relayagent" title="RelayAgent">RelayAgent</a>" : <i>[ <a href="relayagent.md">RelayAgent</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::NsxvDhcpRelay
Properties:
    <a href="#domainnames" title="DomainNames">DomainNames</a>: <i>
      - String</i>
    <a href="#edgegateway" title="EdgeGateway">EdgeGateway</a>: <i>String</i>
    <a href="#ipaddresses" title="IpAddresses">IpAddresses</a>: <i>
      - String</i>
    <a href="#ipsets" title="IpSets">IpSets</a>: <i>
      - String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
    <a href="#relayagent" title="RelayAgent">RelayAgent</a>: <i>
      - <a href="relayagent.md">RelayAgent</a></i>
</pre>

## Properties

#### DomainNames

A set of domain names.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeGateway

The name of the edge gateway on which DHCP relay is to be configured.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddresses

A set of IP addresses.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpSets

A set of IP set names.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful
when connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC to use, optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelayAgent

_Required_: No

_Type_: List of <a href="relayagent.md">RelayAgent</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

