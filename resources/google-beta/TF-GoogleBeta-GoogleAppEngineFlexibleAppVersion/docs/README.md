# TF::GoogleBeta::GoogleAppEngineFlexibleAppVersion

CloudFormation equivalent of google_app_engine_flexible_app_version

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleAppEngineFlexibleAppVersion",
    "Properties" : {
        "<a href="#betasettings" title="BetaSettings">BetaSettings</a>" : <i>[ <a href="betasettingsdefinition.md">BetaSettingsDefinition</a>, ... ]</i>,
        "<a href="#defaultexpiration" title="DefaultExpiration">DefaultExpiration</a>" : <i>String</i>,
        "<a href="#deleteserviceondestroy" title="DeleteServiceOnDestroy">DeleteServiceOnDestroy</a>" : <i>Boolean</i>,
        "<a href="#envvariables" title="EnvVariables">EnvVariables</a>" : <i>[ <a href="envvariablesdefinition.md">EnvVariablesDefinition</a>, ... ]</i>,
        "<a href="#inboundservices" title="InboundServices">InboundServices</a>" : <i>[ String, ... ]</i>,
        "<a href="#instanceclass" title="InstanceClass">InstanceClass</a>" : <i>String</i>,
        "<a href="#nobuildfilesregex" title="NobuildFilesRegex">NobuildFilesRegex</a>" : <i>String</i>,
        "<a href="#noopondestroy" title="NoopOnDestroy">NoopOnDestroy</a>" : <i>Boolean</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#runtime" title="Runtime">Runtime</a>" : <i>String</i>,
        "<a href="#runtimeapiversion" title="RuntimeApiVersion">RuntimeApiVersion</a>" : <i>String</i>,
        "<a href="#runtimechannel" title="RuntimeChannel">RuntimeChannel</a>" : <i>String</i>,
        "<a href="#runtimemainexecutablepath" title="RuntimeMainExecutablePath">RuntimeMainExecutablePath</a>" : <i>String</i>,
        "<a href="#service" title="Service">Service</a>" : <i>String</i>,
        "<a href="#servingstatus" title="ServingStatus">ServingStatus</a>" : <i>String</i>,
        "<a href="#versionid" title="VersionId">VersionId</a>" : <i>String</i>,
        "<a href="#apiconfig" title="ApiConfig">ApiConfig</a>" : <i>[ <a href="apiconfigdefinition.md">ApiConfigDefinition</a>, ... ]</i>,
        "<a href="#automaticscaling" title="AutomaticScaling">AutomaticScaling</a>" : <i>[ <a href="automaticscalingdefinition.md">AutomaticScalingDefinition</a>, ... ]</i>,
        "<a href="#deployment" title="Deployment">Deployment</a>" : <i>[ <a href="deploymentdefinition.md">DeploymentDefinition</a>, ... ]</i>,
        "<a href="#endpointsapiservice" title="EndpointsApiService">EndpointsApiService</a>" : <i>[ <a href="endpointsapiservicedefinition.md">EndpointsApiServiceDefinition</a>, ... ]</i>,
        "<a href="#entrypoint" title="Entrypoint">Entrypoint</a>" : <i>[ <a href="entrypointdefinition.md">EntrypointDefinition</a>, ... ]</i>,
        "<a href="#handlers" title="Handlers">Handlers</a>" : <i>[ <a href="handlersdefinition.md">HandlersDefinition</a>, ... ]</i>,
        "<a href="#livenesscheck" title="LivenessCheck">LivenessCheck</a>" : <i>[ <a href="livenesscheckdefinition.md">LivenessCheckDefinition</a>, ... ]</i>,
        "<a href="#manualscaling" title="ManualScaling">ManualScaling</a>" : <i>[ <a href="manualscalingdefinition.md">ManualScalingDefinition</a>, ... ]</i>,
        "<a href="#network" title="Network">Network</a>" : <i>[ <a href="networkdefinition.md">NetworkDefinition</a>, ... ]</i>,
        "<a href="#readinesscheck" title="ReadinessCheck">ReadinessCheck</a>" : <i>[ <a href="readinesscheckdefinition.md">ReadinessCheckDefinition</a>, ... ]</i>,
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ <a href="resourcesdefinition.md">ResourcesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#vpcaccessconnector" title="VpcAccessConnector">VpcAccessConnector</a>" : <i>[ <a href="vpcaccessconnectordefinition.md">VpcAccessConnectorDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleAppEngineFlexibleAppVersion
Properties:
    <a href="#betasettings" title="BetaSettings">BetaSettings</a>: <i>
      - <a href="betasettingsdefinition.md">BetaSettingsDefinition</a></i>
    <a href="#defaultexpiration" title="DefaultExpiration">DefaultExpiration</a>: <i>String</i>
    <a href="#deleteserviceondestroy" title="DeleteServiceOnDestroy">DeleteServiceOnDestroy</a>: <i>Boolean</i>
    <a href="#envvariables" title="EnvVariables">EnvVariables</a>: <i>
      - <a href="envvariablesdefinition.md">EnvVariablesDefinition</a></i>
    <a href="#inboundservices" title="InboundServices">InboundServices</a>: <i>
      - String</i>
    <a href="#instanceclass" title="InstanceClass">InstanceClass</a>: <i>String</i>
    <a href="#nobuildfilesregex" title="NobuildFilesRegex">NobuildFilesRegex</a>: <i>String</i>
    <a href="#noopondestroy" title="NoopOnDestroy">NoopOnDestroy</a>: <i>Boolean</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#runtime" title="Runtime">Runtime</a>: <i>String</i>
    <a href="#runtimeapiversion" title="RuntimeApiVersion">RuntimeApiVersion</a>: <i>String</i>
    <a href="#runtimechannel" title="RuntimeChannel">RuntimeChannel</a>: <i>String</i>
    <a href="#runtimemainexecutablepath" title="RuntimeMainExecutablePath">RuntimeMainExecutablePath</a>: <i>String</i>
    <a href="#service" title="Service">Service</a>: <i>String</i>
    <a href="#servingstatus" title="ServingStatus">ServingStatus</a>: <i>String</i>
    <a href="#versionid" title="VersionId">VersionId</a>: <i>String</i>
    <a href="#apiconfig" title="ApiConfig">ApiConfig</a>: <i>
      - <a href="apiconfigdefinition.md">ApiConfigDefinition</a></i>
    <a href="#automaticscaling" title="AutomaticScaling">AutomaticScaling</a>: <i>
      - <a href="automaticscalingdefinition.md">AutomaticScalingDefinition</a></i>
    <a href="#deployment" title="Deployment">Deployment</a>: <i>
      - <a href="deploymentdefinition.md">DeploymentDefinition</a></i>
    <a href="#endpointsapiservice" title="EndpointsApiService">EndpointsApiService</a>: <i>
      - <a href="endpointsapiservicedefinition.md">EndpointsApiServiceDefinition</a></i>
    <a href="#entrypoint" title="Entrypoint">Entrypoint</a>: <i>
      - <a href="entrypointdefinition.md">EntrypointDefinition</a></i>
    <a href="#handlers" title="Handlers">Handlers</a>: <i>
      - <a href="handlersdefinition.md">HandlersDefinition</a></i>
    <a href="#livenesscheck" title="LivenessCheck">LivenessCheck</a>: <i>
      - <a href="livenesscheckdefinition.md">LivenessCheckDefinition</a></i>
    <a href="#manualscaling" title="ManualScaling">ManualScaling</a>: <i>
      - <a href="manualscalingdefinition.md">ManualScalingDefinition</a></i>
    <a href="#network" title="Network">Network</a>: <i>
      - <a href="networkdefinition.md">NetworkDefinition</a></i>
    <a href="#readinesscheck" title="ReadinessCheck">ReadinessCheck</a>: <i>
      - <a href="readinesscheckdefinition.md">ReadinessCheckDefinition</a></i>
    <a href="#resources" title="Resources">Resources</a>: <i>
      - <a href="resourcesdefinition.md">ResourcesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#vpcaccessconnector" title="VpcAccessConnector">VpcAccessConnector</a>: <i>
      - <a href="vpcaccessconnectordefinition.md">VpcAccessConnectorDefinition</a></i>
</pre>

## Properties

#### BetaSettings

_Required_: No

_Type_: List of <a href="betasettingsdefinition.md">BetaSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultExpiration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteServiceOnDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvVariables

_Required_: No

_Type_: List of <a href="envvariablesdefinition.md">EnvVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InboundServices

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceClass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NobuildFilesRegex

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoopOnDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuntimeApiVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuntimeChannel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuntimeMainExecutablePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServingStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiConfig

_Required_: No

_Type_: List of <a href="apiconfigdefinition.md">ApiConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomaticScaling

_Required_: No

_Type_: List of <a href="automaticscalingdefinition.md">AutomaticScalingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deployment

_Required_: No

_Type_: List of <a href="deploymentdefinition.md">DeploymentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointsApiService

_Required_: No

_Type_: List of <a href="endpointsapiservicedefinition.md">EndpointsApiServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entrypoint

_Required_: No

_Type_: List of <a href="entrypointdefinition.md">EntrypointDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Handlers

_Required_: No

_Type_: List of <a href="handlersdefinition.md">HandlersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LivenessCheck

_Required_: No

_Type_: List of <a href="livenesscheckdefinition.md">LivenessCheckDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManualScaling

_Required_: No

_Type_: List of <a href="manualscalingdefinition.md">ManualScalingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="networkdefinition.md">NetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadinessCheck

_Required_: No

_Type_: List of <a href="readinesscheckdefinition.md">ReadinessCheckDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of <a href="resourcesdefinition.md">ResourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcAccessConnector

_Required_: No

_Type_: List of <a href="vpcaccessconnectordefinition.md">VpcAccessConnectorDefinition</a>

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

#### Name

Returns the <code>Name</code> value.

