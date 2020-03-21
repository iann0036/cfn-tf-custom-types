# Terraform::OpenTelekomCloud::AntiddosV1

Anti-DDoS monitors the service traffic from the Internet to ECSs, ELB instances, and BMSs to detect attack traffic in real time. It then cleans attack traffic according to user-configured defense policies so that services run as normal.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::AntiddosV1",
    "Properties" : {
        "<a href="#apptypeid" title="AppTypeId">AppTypeId</a>" : <i>Double</i>,
        "<a href="#cleaningaccessposid" title="CleaningAccessPosId">CleaningAccessPosId</a>" : <i>Double</i>,
        "<a href="#enablel7" title="EnableL7">EnableL7</a>" : <i>Boolean</i>,
        "<a href="#floatingipid" title="FloatingIpId">FloatingIpId</a>" : <i>String</i>,
        "<a href="#httprequestposid" title="HttpRequestPosId">HttpRequestPosId</a>" : <i>Double</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#trafficposid" title="TrafficPosId">TrafficPosId</a>" : <i>Double</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::AntiddosV1
Properties:
    <a href="#apptypeid" title="AppTypeId">AppTypeId</a>: <i>Double</i>
    <a href="#cleaningaccessposid" title="CleaningAccessPosId">CleaningAccessPosId</a>: <i>Double</i>
    <a href="#enablel7" title="EnableL7">EnableL7</a>: <i>Boolean</i>
    <a href="#floatingipid" title="FloatingIpId">FloatingIpId</a>: <i>String</i>
    <a href="#httprequestposid" title="HttpRequestPosId">HttpRequestPosId</a>: <i>Double</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#trafficposid" title="TrafficPosId">TrafficPosId</a>: <i>Double</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AppTypeId

The application type ID.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CleaningAccessPosId

The position ID of access limit during cleaning. The value ranges from 1 to 8.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableL7

Specifies whether to enable L7 defense.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingIpId

The ID corresponding to the Elastic IP Address (EIP) of a user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRequestPosId

The position ID of number of HTTP requests. The value ranges from 1 to 15.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficPosId

The position ID of traffic. The value ranges from 1 to 9.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

