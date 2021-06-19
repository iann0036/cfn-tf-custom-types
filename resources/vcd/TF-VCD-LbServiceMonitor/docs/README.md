# TF::VCD::LbServiceMonitor

Provides a vCloud Director Edge Gateway Load Balancer Service Monitor resource. A service monitor 
defines health check parameters for a particular type of network traffic. It can be associated with
a pool. Pool members are monitored according to the service monitor parameters. 

~> **Note:** To make load balancing work one must ensure that load balancing is enabled on edge gateway (edge gateway must be advanced).
This depends on NSX version to work properly. Please refer to [VMware Product Interoperability Matrices](https://www.vmware.com/resources/compatibility/sim/interop_matrix.php#interop&29=&93=) 
to check supported vCloud director and NSX for vSphere configurations.

~> **Note:** The vCloud Director API for NSX supports a subset of the operations and objects defined in the NSX vSphere 
API Guide. The API supports NSX 6.2, 6.3, and 6.4.

Supported in provider *v2.4+*

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VCD::LbServiceMonitor",
    "Properties" : {
        "<a href="#edgegateway" title="EdgeGateway">EdgeGateway</a>" : <i>String</i>,
        "<a href="#expected" title="Expected">Expected</a>" : <i>String</i>,
        "<a href="#extension" title="Extension">Extension</a>" : <i>[ <a href="extensiondefinition.md">ExtensionDefinition</a>, ... ]</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
        "<a href="#maxretries" title="MaxRetries">MaxRetries</a>" : <i>Double</i>,
        "<a href="#method" title="Method">Method</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#receive" title="Receive">Receive</a>" : <i>String</i>,
        "<a href="#send" title="Send">Send</a>" : <i>String</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VCD::LbServiceMonitor
Properties:
    <a href="#edgegateway" title="EdgeGateway">EdgeGateway</a>: <i>String</i>
    <a href="#expected" title="Expected">Expected</a>: <i>String</i>
    <a href="#extension" title="Extension">Extension</a>: <i>
      - <a href="extensiondefinition.md">ExtensionDefinition</a></i>
    <a href="#interval" title="Interval">Interval</a>: <i>Double</i>
    <a href="#maxretries" title="MaxRetries">MaxRetries</a>: <i>Double</i>
    <a href="#method" title="Method">Method</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#receive" title="Receive">Receive</a>: <i>String</i>
    <a href="#send" title="Send">Send</a>: <i>String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
</pre>

## Properties

#### EdgeGateway

The name of the edge gateway on which the service monitor is to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expected

For types `http` and `https`. String that the monitor expects to match in the status line of
the HTTP or HTTPS response (for example, `HTTP/1.1`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extension

A map of advanced monitor parameters as key=value pairs (i.e. `max-age=SECONDS`, `invert-regex`)
**Note**: When you need a value of `key` only format just set value to empty string (i.e. `linespan = ""`).

_Required_: No

_Type_: List of <a href="extensiondefinition.md">ExtensionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

Interval in seconds at which a server is to be monitored using the specified Method.
Defaults to 10.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRetries

Number of times the specified monitoring Method must fail sequentially before the server is
declared down. Defaults to 3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

For types `http` and `https`. Select http method to be used to detect server status. One of
OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, or CONNECT.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Service Monitor name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Receive

For types `http`,  `https`, and `udp`. The string to be matched in the response content.
**Note**: When `expected` is not matched, the monitor does not try to match the Receive content.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Send

For types `http`,  `https`, and `udp`. The data to be sent.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Maximum time in seconds within which a response from the server must be received. Defaults to 15.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Select the way in which you want to send the health check request to the server — `http`, `https`,
`tcp`, `icmp`, or `udp`. Depending on the type selected, the remaining attributes are allowed or not.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

For types `http` and `https`. URL to be used in the server status request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC to use, optional if defined at provider level.

_Required_: No

_Type_: String

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

