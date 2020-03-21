# Terraform::AzureRM::ApiManagementApiOperation

Manages an API Operation within an API Management Service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ApiManagementApiOperation",
    "Properties" : {
        "<a href="#apimanagementname" title="ApiManagementName">ApiManagementName</a>" : <i>String</i>,
        "<a href="#apiname" title="ApiName">ApiName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#method" title="Method">Method</a>" : <i>String</i>,
        "<a href="#operationid" title="OperationId">OperationId</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#urltemplate" title="UrlTemplate">UrlTemplate</a>" : <i>String</i>,
        "<a href="#request" title="Request">Request</a>" : <i>[ <a href="request.md">Request</a>, ... ]</i>,
        "<a href="#response" title="Response">Response</a>" : <i>[ <a href="response.md">Response</a>, ... ]</i>,
        "<a href="#templateparameter" title="TemplateParameter">TemplateParameter</a>" : <i>[ <a href="templateparameter.md">TemplateParameter</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#header" title="Header">Header</a>" : <i>[ <a href="header.md">Header</a>, ... ]</i>,
        "<a href="#queryparameter" title="QueryParameter">QueryParameter</a>" : <i>[ <a href="queryparameter.md">QueryParameter</a>, ... ]</i>,
        "<a href="#representation" title="Representation">Representation</a>" : <i>[ <a href="representation.md">Representation</a>, ... ]</i>,
        "<a href="#formparameter" title="FormParameter">FormParameter</a>" : <i>[ <a href="formparameter.md">FormParameter</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ApiManagementApiOperation
Properties:
    <a href="#apimanagementname" title="ApiManagementName">ApiManagementName</a>: <i>String</i>
    <a href="#apiname" title="ApiName">ApiName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#method" title="Method">Method</a>: <i>String</i>
    <a href="#operationid" title="OperationId">OperationId</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#urltemplate" title="UrlTemplate">UrlTemplate</a>: <i>String</i>
    <a href="#request" title="Request">Request</a>: <i>
      - <a href="request.md">Request</a></i>
    <a href="#response" title="Response">Response</a>: <i>
      - <a href="response.md">Response</a></i>
    <a href="#templateparameter" title="TemplateParameter">TemplateParameter</a>: <i>
      - <a href="templateparameter.md">TemplateParameter</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#header" title="Header">Header</a>: <i>
      - <a href="header.md">Header</a></i>
    <a href="#queryparameter" title="QueryParameter">QueryParameter</a>: <i>
      - <a href="queryparameter.md">QueryParameter</a></i>
    <a href="#representation" title="Representation">Representation</a>: <i>
      - <a href="representation.md">Representation</a></i>
    <a href="#formparameter" title="FormParameter">FormParameter</a>: <i>
      - <a href="formparameter.md">FormParameter</a></i>
</pre>

## Properties

#### ApiManagementName

The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiName

The name of the API within the API Management Service where this API Operation should be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of this Query Parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The Display Name for this API Management Operation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

The HTTP Method used for this API Management Operation, like `GET`, `DELETE`, `PUT` or `POST` - but not limited to these values.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperationId

A unique identifier for this API Operation. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlTemplate

The relative URL Template identifying the target resource for this operation, which may include parameters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Request

_Required_: No

_Type_: List of <a href="request.md">Request</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Response

_Required_: No

_Type_: List of <a href="response.md">Response</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateParameter

_Required_: No

_Type_: List of <a href="templateparameter.md">TemplateParameter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No

_Type_: List of <a href="header.md">Header</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryParameter

_Required_: No

_Type_: List of <a href="queryparameter.md">QueryParameter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Representation

_Required_: No

_Type_: List of <a href="representation.md">Representation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FormParameter

_Required_: No

_Type_: List of <a href="formparameter.md">FormParameter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

