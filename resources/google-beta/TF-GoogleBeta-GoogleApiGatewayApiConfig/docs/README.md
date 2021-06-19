# TF::GoogleBeta::GoogleApiGatewayApiConfig

CloudFormation equivalent of google_api_gateway_api_config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleApiGatewayApiConfig",
    "Properties" : {
        "<a href="#api" title="Api">Api</a>" : <i>String</i>,
        "<a href="#apiconfigid" title="ApiConfigId">ApiConfigId</a>" : <i>String</i>,
        "<a href="#apiconfigidprefix" title="ApiConfigIdPrefix">ApiConfigIdPrefix</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#gatewayconfig" title="GatewayConfig">GatewayConfig</a>" : <i>[ <a href="gatewayconfigdefinition.md">GatewayConfigDefinition</a>, ... ]</i>,
        "<a href="#openapidocuments" title="OpenapiDocuments">OpenapiDocuments</a>" : <i>[ <a href="openapidocumentsdefinition.md">OpenapiDocumentsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleApiGatewayApiConfig
Properties:
    <a href="#api" title="Api">Api</a>: <i>String</i>
    <a href="#apiconfigid" title="ApiConfigId">ApiConfigId</a>: <i>String</i>
    <a href="#apiconfigidprefix" title="ApiConfigIdPrefix">ApiConfigIdPrefix</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#gatewayconfig" title="GatewayConfig">GatewayConfig</a>: <i>
      - <a href="gatewayconfigdefinition.md">GatewayConfigDefinition</a></i>
    <a href="#openapidocuments" title="OpenapiDocuments">OpenapiDocuments</a>: <i>
      - <a href="openapidocumentsdefinition.md">OpenapiDocumentsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Api

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiConfigId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiConfigIdPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayConfig

_Required_: No

_Type_: List of <a href="gatewayconfigdefinition.md">GatewayConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenapiDocuments

_Required_: No

_Type_: List of <a href="openapidocumentsdefinition.md">OpenapiDocumentsDefinition</a>

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

#### Name

Returns the <code>Name</code> value.

#### ServiceConfigId

Returns the <code>ServiceConfigId</code> value.

