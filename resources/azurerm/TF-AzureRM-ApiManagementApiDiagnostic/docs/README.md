# TF::AzureRM::ApiManagementApiDiagnostic

Manages a API Management Service API Diagnostics Logs.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::ApiManagementApiDiagnostic",
    "Properties" : {
        "<a href="#alwayslogerrors" title="AlwaysLogErrors">AlwaysLogErrors</a>" : <i>Boolean</i>,
        "<a href="#apimanagementloggerid" title="ApiManagementLoggerId">ApiManagementLoggerId</a>" : <i>String</i>,
        "<a href="#apimanagementname" title="ApiManagementName">ApiManagementName</a>" : <i>String</i>,
        "<a href="#apiname" title="ApiName">ApiName</a>" : <i>String</i>,
        "<a href="#httpcorrelationprotocol" title="HttpCorrelationProtocol">HttpCorrelationProtocol</a>" : <i>String</i>,
        "<a href="#identifier" title="Identifier">Identifier</a>" : <i>String</i>,
        "<a href="#logclientip" title="LogClientIp">LogClientIp</a>" : <i>Boolean</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#samplingpercentage" title="SamplingPercentage">SamplingPercentage</a>" : <i>Double</i>,
        "<a href="#verbosity" title="Verbosity">Verbosity</a>" : <i>String</i>,
        "<a href="#backendrequest" title="BackendRequest">BackendRequest</a>" : <i>[ <a href="backendrequestdefinition.md">BackendRequestDefinition</a>, ... ]</i>,
        "<a href="#backendresponse" title="BackendResponse">BackendResponse</a>" : <i>[ <a href="backendresponsedefinition.md">BackendResponseDefinition</a>, ... ]</i>,
        "<a href="#frontendrequest" title="FrontendRequest">FrontendRequest</a>" : <i>[ <a href="frontendrequestdefinition.md">FrontendRequestDefinition</a>, ... ]</i>,
        "<a href="#frontendresponse" title="FrontendResponse">FrontendResponse</a>" : <i>[ <a href="frontendresponsedefinition.md">FrontendResponseDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::ApiManagementApiDiagnostic
Properties:
    <a href="#alwayslogerrors" title="AlwaysLogErrors">AlwaysLogErrors</a>: <i>Boolean</i>
    <a href="#apimanagementloggerid" title="ApiManagementLoggerId">ApiManagementLoggerId</a>: <i>String</i>
    <a href="#apimanagementname" title="ApiManagementName">ApiManagementName</a>: <i>String</i>
    <a href="#apiname" title="ApiName">ApiName</a>: <i>String</i>
    <a href="#httpcorrelationprotocol" title="HttpCorrelationProtocol">HttpCorrelationProtocol</a>: <i>String</i>
    <a href="#identifier" title="Identifier">Identifier</a>: <i>String</i>
    <a href="#logclientip" title="LogClientIp">LogClientIp</a>: <i>Boolean</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#samplingpercentage" title="SamplingPercentage">SamplingPercentage</a>: <i>Double</i>
    <a href="#verbosity" title="Verbosity">Verbosity</a>: <i>String</i>
    <a href="#backendrequest" title="BackendRequest">BackendRequest</a>: <i>
      - <a href="backendrequestdefinition.md">BackendRequestDefinition</a></i>
    <a href="#backendresponse" title="BackendResponse">BackendResponse</a>: <i>
      - <a href="backendresponsedefinition.md">BackendResponseDefinition</a></i>
    <a href="#frontendrequest" title="FrontendRequest">FrontendRequest</a>: <i>
      - <a href="frontendrequestdefinition.md">FrontendRequestDefinition</a></i>
    <a href="#frontendresponse" title="FrontendResponse">FrontendResponse</a>: <i>
      - <a href="frontendresponsedefinition.md">FrontendResponseDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AlwaysLogErrors

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiManagementLoggerId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiManagementName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpCorrelationProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identifier

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogClientIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamplingPercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Verbosity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendRequest

_Required_: No

_Type_: List of <a href="backendrequestdefinition.md">BackendRequestDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendResponse

_Required_: No

_Type_: List of <a href="backendresponsedefinition.md">BackendResponseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendRequest

_Required_: No

_Type_: List of <a href="frontendrequestdefinition.md">FrontendRequestDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendResponse

_Required_: No

_Type_: List of <a href="frontendresponsedefinition.md">FrontendResponseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

