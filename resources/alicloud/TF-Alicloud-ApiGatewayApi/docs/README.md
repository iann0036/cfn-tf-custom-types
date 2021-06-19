# TF::Alicloud::ApiGatewayApi

Provides an api resource.When you create an API, you must enter the basic information about the API, and define the API request information, the API backend service and response information.

For information about Api Gateway Api and how to use it, see [Create an API](https://www.alibabacloud.com/help/doc-detail/29478.htm)

-> **NOTE:** Terraform will auto build api while it uses `alicloud_api_gateway_api` to build api.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::ApiGatewayApi",
    "Properties" : {
        "<a href="#authtype" title="AuthType">AuthType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#servicetype" title="ServiceType">ServiceType</a>" : <i>String</i>,
        "<a href="#stagenames" title="StageNames">StageNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#constantparameters" title="ConstantParameters">ConstantParameters</a>" : <i>[ <a href="constantparametersdefinition.md">ConstantParametersDefinition</a>, ... ]</i>,
        "<a href="#fcserviceconfig" title="FcServiceConfig">FcServiceConfig</a>" : <i>[ <a href="fcserviceconfigdefinition.md">FcServiceConfigDefinition</a>, ... ]</i>,
        "<a href="#httpserviceconfig" title="HttpServiceConfig">HttpServiceConfig</a>" : <i>[ <a href="httpserviceconfigdefinition.md">HttpServiceConfigDefinition</a>, ... ]</i>,
        "<a href="#httpvpcserviceconfig" title="HttpVpcServiceConfig">HttpVpcServiceConfig</a>" : <i>[ <a href="httpvpcserviceconfigdefinition.md">HttpVpcServiceConfigDefinition</a>, ... ]</i>,
        "<a href="#mockserviceconfig" title="MockServiceConfig">MockServiceConfig</a>" : <i>[ <a href="mockserviceconfigdefinition.md">MockServiceConfigDefinition</a>, ... ]</i>,
        "<a href="#requestconfig" title="RequestConfig">RequestConfig</a>" : <i>[ <a href="requestconfigdefinition.md">RequestConfigDefinition</a>, ... ]</i>,
        "<a href="#requestparameters" title="RequestParameters">RequestParameters</a>" : <i>[ <a href="requestparametersdefinition.md">RequestParametersDefinition</a>, ... ]</i>,
        "<a href="#systemparameters" title="SystemParameters">SystemParameters</a>" : <i>[ <a href="systemparametersdefinition.md">SystemParametersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::ApiGatewayApi
Properties:
    <a href="#authtype" title="AuthType">AuthType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#servicetype" title="ServiceType">ServiceType</a>: <i>String</i>
    <a href="#stagenames" title="StageNames">StageNames</a>: <i>
      - String</i>
    <a href="#constantparameters" title="ConstantParameters">ConstantParameters</a>: <i>
      - <a href="constantparametersdefinition.md">ConstantParametersDefinition</a></i>
    <a href="#fcserviceconfig" title="FcServiceConfig">FcServiceConfig</a>: <i>
      - <a href="fcserviceconfigdefinition.md">FcServiceConfigDefinition</a></i>
    <a href="#httpserviceconfig" title="HttpServiceConfig">HttpServiceConfig</a>: <i>
      - <a href="httpserviceconfigdefinition.md">HttpServiceConfigDefinition</a></i>
    <a href="#httpvpcserviceconfig" title="HttpVpcServiceConfig">HttpVpcServiceConfig</a>: <i>
      - <a href="httpvpcserviceconfigdefinition.md">HttpVpcServiceConfigDefinition</a></i>
    <a href="#mockserviceconfig" title="MockServiceConfig">MockServiceConfig</a>: <i>
      - <a href="mockserviceconfigdefinition.md">MockServiceConfigDefinition</a></i>
    <a href="#requestconfig" title="RequestConfig">RequestConfig</a>: <i>
      - <a href="requestconfigdefinition.md">RequestConfigDefinition</a></i>
    <a href="#requestparameters" title="RequestParameters">RequestParameters</a>: <i>
      - <a href="requestparametersdefinition.md">RequestParametersDefinition</a></i>
    <a href="#systemparameters" title="SystemParameters">SystemParameters</a>: <i>
      - <a href="systemparametersdefinition.md">SystemParametersDefinition</a></i>
</pre>

## Properties

#### AuthType

The authorization Type including APP and ANONYMOUS. Defaults to null.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the api. Defaults to null.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

The api gateway that the api belongs to. Defaults to null.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the api gateway api. Defaults to null.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceType

The type of backend service. Type including HTTP,VPC and MOCK. Defaults to null.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StageNames

Stages that the api need to be deployed. Valid value: RELEASE | PRE | TEST.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConstantParameters

_Required_: No

_Type_: List of <a href="constantparametersdefinition.md">ConstantParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FcServiceConfig

_Required_: No

_Type_: List of <a href="fcserviceconfigdefinition.md">FcServiceConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpServiceConfig

_Required_: No

_Type_: List of <a href="httpserviceconfigdefinition.md">HttpServiceConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpVpcServiceConfig

_Required_: No

_Type_: List of <a href="httpvpcserviceconfigdefinition.md">HttpVpcServiceConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MockServiceConfig

_Required_: No

_Type_: List of <a href="mockserviceconfigdefinition.md">MockServiceConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestConfig

_Required_: No

_Type_: List of <a href="requestconfigdefinition.md">RequestConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestParameters

_Required_: No

_Type_: List of <a href="requestparametersdefinition.md">RequestParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemParameters

_Required_: No

_Type_: List of <a href="systemparametersdefinition.md">SystemParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiId

Returns the <code>ApiId</code> value.

#### Id

Returns the <code>Id</code> value.

