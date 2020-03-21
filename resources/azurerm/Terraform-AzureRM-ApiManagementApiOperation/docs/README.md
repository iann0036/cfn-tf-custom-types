# Terraform::AzureRM::ApiManagementApiOperation

CloudFormation equivalent of azurerm_api_management_api_operation

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ApiManagementApiOperation",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#apimanagementname" title="ApiManagementName">ApiManagementName</a>" : <i>String</i>,
        "<a href="#apiname" title="ApiName">ApiName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#method" title="Method">Method</a>" : <i>String</i>,
        "<a href="#operationid" title="OperationId">OperationId</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#urltemplate" title="UrlTemplate">UrlTemplate</a>" : <i>String</i>,
        "<a href="#request" title="Request">Request</a>" : <i>[ &lt;a href=&#34;request.md&#34;&gt;Request&lt;/a&gt;, ... ]</i>,
        "<a href="#response" title="Response">Response</a>" : <i>[ &lt;a href=&#34;response.md&#34;&gt;Response&lt;/a&gt;, ... ]</i>,
        "<a href="#templateparameter" title="TemplateParameter">TemplateParameter</a>" : <i>[ &lt;a href=&#34;templateparameter.md&#34;&gt;TemplateParameter&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#header" title="Header">Header</a>" : <i>[ &lt;a href=&#34;header.md&#34;&gt;Header&lt;/a&gt;, ... ]</i>,
        "<a href="#queryparameter" title="QueryParameter">QueryParameter</a>" : <i>[ &lt;a href=&#34;queryparameter.md&#34;&gt;QueryParameter&lt;/a&gt;, ... ]</i>,
        "<a href="#representation" title="Representation">Representation</a>" : <i>[ &lt;a href=&#34;representation.md&#34;&gt;Representation&lt;/a&gt;, ... ]</i>,
        "<a href="#formparameter" title="FormParameter">FormParameter</a>" : <i>[ &lt;a href=&#34;formparameter.md&#34;&gt;FormParameter&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ApiManagementApiOperation
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#apimanagementname" title="ApiManagementName">ApiManagementName</a>: <i>String</i>
    <a href="#apiname" title="ApiName">ApiName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#method" title="Method">Method</a>: <i>String</i>
    <a href="#operationid" title="OperationId">OperationId</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#urltemplate" title="UrlTemplate">UrlTemplate</a>: <i>String</i>
    <a href="#request" title="Request">Request</a>: <i>
      - &lt;a href=&#34;request.md&#34;&gt;Request&lt;/a&gt;</i>
    <a href="#response" title="Response">Response</a>: <i>
      - &lt;a href=&#34;response.md&#34;&gt;Response&lt;/a&gt;</i>
    <a href="#templateparameter" title="TemplateParameter">TemplateParameter</a>: <i>
      - &lt;a href=&#34;templateparameter.md&#34;&gt;TemplateParameter&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#header" title="Header">Header</a>: <i>
      - &lt;a href=&#34;header.md&#34;&gt;Header&lt;/a&gt;</i>
    <a href="#queryparameter" title="QueryParameter">QueryParameter</a>: <i>
      - &lt;a href=&#34;queryparameter.md&#34;&gt;QueryParameter&lt;/a&gt;</i>
    <a href="#representation" title="Representation">Representation</a>: <i>
      - &lt;a href=&#34;representation.md&#34;&gt;Representation&lt;/a&gt;</i>
    <a href="#formparameter" title="FormParameter">FormParameter</a>: <i>
      - &lt;a href=&#34;formparameter.md&#34;&gt;FormParameter&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

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

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperationId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlTemplate

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Request

_Required_: No

_Type_: List of &lt;a href=&#34;request.md&#34;&gt;Request&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Response

_Required_: No

_Type_: List of &lt;a href=&#34;response.md&#34;&gt;Response&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateParameter

_Required_: No

_Type_: List of &lt;a href=&#34;templateparameter.md&#34;&gt;TemplateParameter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No

_Type_: List of &lt;a href=&#34;header.md&#34;&gt;Header&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryParameter

_Required_: No

_Type_: List of &lt;a href=&#34;queryparameter.md&#34;&gt;QueryParameter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Representation

_Required_: No

_Type_: List of &lt;a href=&#34;representation.md&#34;&gt;Representation&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FormParameter

_Required_: No

_Type_: List of &lt;a href=&#34;formparameter.md&#34;&gt;FormParameter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

