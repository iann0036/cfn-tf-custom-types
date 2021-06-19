# TF::AzureRM::ApiManagementDiagnostic

Manages an API Management Service Diagnostic.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::ApiManagementDiagnostic",
    "Properties" : {
        "<a href="#alwayslogerrors" title="AlwaysLogErrors">AlwaysLogErrors</a>" : <i>Boolean</i>,
        "<a href="#apimanagementloggerid" title="ApiManagementLoggerId">ApiManagementLoggerId</a>" : <i>String</i>,
        "<a href="#apimanagementname" title="ApiManagementName">ApiManagementName</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
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
Type: TF::AzureRM::ApiManagementDiagnostic
Properties:
    <a href="#alwayslogerrors" title="AlwaysLogErrors">AlwaysLogErrors</a>: <i>Boolean</i>
    <a href="#apimanagementloggerid" title="ApiManagementLoggerId">ApiManagementLoggerId</a>: <i>String</i>
    <a href="#apimanagementname" title="ApiManagementName">ApiManagementName</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
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

Always log errors. Send telemetry if there is an erroneous condition, regardless of sampling settings.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiManagementLoggerId

The id of the target API Management Logger where the API Management Diagnostic should be saved.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiManagementName

The Name of the API Management Service where this Diagnostic should be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpCorrelationProtocol

The HTTP Correlation Protocol to use. Possible values are `None`, `Legacy` or `W3C`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identifier

The diagnostic identifier for the API Management Service. At this time the only supported value is `applicationinsights`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogClientIp

Log client IP address.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamplingPercentage

Sampling (%). For high traffic APIs, please read this [documentation](https://docs.microsoft.com/azure/api-management/api-management-howto-app-insights#performance-implications-and-log-sampling) to understand performance implications and log sampling. Valid values are between `0.0` and `100.0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Verbosity

Logging verbosity. Possible values are `verbose`, `information` or `error`.

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

