# TF::TencentCloud::ApiGatewayApi

Use this resource to create API of API gateway.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::ApiGatewayApi",
    "Properties" : {
        "<a href="#apidesc" title="ApiDesc">ApiDesc</a>" : <i>String</i>,
        "<a href="#apiname" title="ApiName">ApiName</a>" : <i>String</i>,
        "<a href="#authtype" title="AuthType">AuthType</a>" : <i>String</i>,
        "<a href="#enablecors" title="EnableCors">EnableCors</a>" : <i>Boolean</i>,
        "<a href="#prelimit" title="PreLimit">PreLimit</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#releaselimit" title="ReleaseLimit">ReleaseLimit</a>" : <i>Double</i>,
        "<a href="#requestconfigmethod" title="RequestConfigMethod">RequestConfigMethod</a>" : <i>String</i>,
        "<a href="#requestconfigpath" title="RequestConfigPath">RequestConfigPath</a>" : <i>String</i>,
        "<a href="#responsefailexample" title="ResponseFailExample">ResponseFailExample</a>" : <i>String</i>,
        "<a href="#responsesuccessexample" title="ResponseSuccessExample">ResponseSuccessExample</a>" : <i>String</i>,
        "<a href="#responsetype" title="ResponseType">ResponseType</a>" : <i>String</i>,
        "<a href="#serviceconfigmethod" title="ServiceConfigMethod">ServiceConfigMethod</a>" : <i>String</i>,
        "<a href="#serviceconfigmockreturnmessage" title="ServiceConfigMockReturnMessage">ServiceConfigMockReturnMessage</a>" : <i>String</i>,
        "<a href="#serviceconfigpath" title="ServiceConfigPath">ServiceConfigPath</a>" : <i>String</i>,
        "<a href="#serviceconfigproduct" title="ServiceConfigProduct">ServiceConfigProduct</a>" : <i>String</i>,
        "<a href="#serviceconfigscffunctionname" title="ServiceConfigScfFunctionName">ServiceConfigScfFunctionName</a>" : <i>String</i>,
        "<a href="#serviceconfigscffunctionnamespace" title="ServiceConfigScfFunctionNamespace">ServiceConfigScfFunctionNamespace</a>" : <i>String</i>,
        "<a href="#serviceconfigscffunctionqualifier" title="ServiceConfigScfFunctionQualifier">ServiceConfigScfFunctionQualifier</a>" : <i>String</i>,
        "<a href="#serviceconfigtimeout" title="ServiceConfigTimeout">ServiceConfigTimeout</a>" : <i>Double</i>,
        "<a href="#serviceconfigtype" title="ServiceConfigType">ServiceConfigType</a>" : <i>String</i>,
        "<a href="#serviceconfigurl" title="ServiceConfigUrl">ServiceConfigUrl</a>" : <i>String</i>,
        "<a href="#serviceconfigvpcid" title="ServiceConfigVpcId">ServiceConfigVpcId</a>" : <i>String</i>,
        "<a href="#serviceid" title="ServiceId">ServiceId</a>" : <i>String</i>,
        "<a href="#testlimit" title="TestLimit">TestLimit</a>" : <i>Double</i>,
        "<a href="#requestparameters" title="RequestParameters">RequestParameters</a>" : <i>[ <a href="requestparametersdefinition.md">RequestParametersDefinition</a>, ... ]</i>,
        "<a href="#responseerrorcodes" title="ResponseErrorCodes">ResponseErrorCodes</a>" : <i>[ <a href="responseerrorcodesdefinition.md">ResponseErrorCodesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::ApiGatewayApi
Properties:
    <a href="#apidesc" title="ApiDesc">ApiDesc</a>: <i>String</i>
    <a href="#apiname" title="ApiName">ApiName</a>: <i>String</i>
    <a href="#authtype" title="AuthType">AuthType</a>: <i>String</i>
    <a href="#enablecors" title="EnableCors">EnableCors</a>: <i>Boolean</i>
    <a href="#prelimit" title="PreLimit">PreLimit</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#releaselimit" title="ReleaseLimit">ReleaseLimit</a>: <i>Double</i>
    <a href="#requestconfigmethod" title="RequestConfigMethod">RequestConfigMethod</a>: <i>String</i>
    <a href="#requestconfigpath" title="RequestConfigPath">RequestConfigPath</a>: <i>String</i>
    <a href="#responsefailexample" title="ResponseFailExample">ResponseFailExample</a>: <i>String</i>
    <a href="#responsesuccessexample" title="ResponseSuccessExample">ResponseSuccessExample</a>: <i>String</i>
    <a href="#responsetype" title="ResponseType">ResponseType</a>: <i>String</i>
    <a href="#serviceconfigmethod" title="ServiceConfigMethod">ServiceConfigMethod</a>: <i>String</i>
    <a href="#serviceconfigmockreturnmessage" title="ServiceConfigMockReturnMessage">ServiceConfigMockReturnMessage</a>: <i>String</i>
    <a href="#serviceconfigpath" title="ServiceConfigPath">ServiceConfigPath</a>: <i>String</i>
    <a href="#serviceconfigproduct" title="ServiceConfigProduct">ServiceConfigProduct</a>: <i>String</i>
    <a href="#serviceconfigscffunctionname" title="ServiceConfigScfFunctionName">ServiceConfigScfFunctionName</a>: <i>String</i>
    <a href="#serviceconfigscffunctionnamespace" title="ServiceConfigScfFunctionNamespace">ServiceConfigScfFunctionNamespace</a>: <i>String</i>
    <a href="#serviceconfigscffunctionqualifier" title="ServiceConfigScfFunctionQualifier">ServiceConfigScfFunctionQualifier</a>: <i>String</i>
    <a href="#serviceconfigtimeout" title="ServiceConfigTimeout">ServiceConfigTimeout</a>: <i>Double</i>
    <a href="#serviceconfigtype" title="ServiceConfigType">ServiceConfigType</a>: <i>String</i>
    <a href="#serviceconfigurl" title="ServiceConfigUrl">ServiceConfigUrl</a>: <i>String</i>
    <a href="#serviceconfigvpcid" title="ServiceConfigVpcId">ServiceConfigVpcId</a>: <i>String</i>
    <a href="#serviceid" title="ServiceId">ServiceId</a>: <i>String</i>
    <a href="#testlimit" title="TestLimit">TestLimit</a>: <i>Double</i>
    <a href="#requestparameters" title="RequestParameters">RequestParameters</a>: <i>
      - <a href="requestparametersdefinition.md">RequestParametersDefinition</a></i>
    <a href="#responseerrorcodes" title="ResponseErrorCodes">ResponseErrorCodes</a>: <i>
      - <a href="responseerrorcodesdefinition.md">ResponseErrorCodesDefinition</a></i>
</pre>

## Properties

#### ApiDesc

Custom API description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiName

Custom API name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthType

API authentication type. Valid values: `SECRET` (key pair authentication),`NONE` (no authentication). Default value: `NONE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableCors

Whether to enable CORS. Default value: `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreLimit

API QPS value. Enter a positive number to limit the API query rate per second `QPS`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

API frontend request type. Valid values: `HTTP`, `WEBSOCKET`. Default value: `HTTP`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReleaseLimit

API QPS value. Enter a positive number to limit the API query rate per second `QPS`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestConfigMethod

Request frontend method configuration. Valid values: `GET`,`POST`,`PUT`,`DELETE`,`HEAD`,`ANY`. Default value: `GET`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestConfigPath

Request frontend path configuration. Like `/user/getinfo`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseFailExample

Response failure sample of custom response configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseSuccessExample

Successful response sample of custom response configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseType

Return type. Valid values: `HTML`, `JSON`, `TEXT`, `BINARY`, `XML`. Default value: `HTML`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConfigMethod

API backend service request method, such as `GET`. If `service_config_type` is `HTTP`, this parameter will be required. The frontend `request_config_method` and backend method `service_config_method` can be different.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConfigMockReturnMessage

Returned information of API backend mocking. This parameter is required when `service_config_type` is `MOCK`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConfigPath

API backend service path, such as /path. If `service_config_type` is `HTTP`, this parameter will be required. The frontend `request_config_path` and backend path `service_config_path` can be different.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConfigProduct

Backend type. This parameter takes effect when VPC is enabled. Currently, only `clb` is supported.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConfigScfFunctionName

SCF function name. This parameter takes effect when `service_config_type` is `SCF`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConfigScfFunctionNamespace

SCF function namespace. This parameter takes effect when `service_config_type` is `SCF`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConfigScfFunctionQualifier

SCF function version. This parameter takes effect when `service_config_type` is `SCF`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConfigTimeout

API backend service timeout period in seconds. Default value: `5`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConfigType

API backend service type. Valid values: `WEBSOCKET`, `HTTP`, `SCF`, `MOCK`. Default value: `HTTP`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConfigUrl

API backend service url. This parameter is required when `service_config_type` is `HTTP`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConfigVpcId

Unique VPC ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceId

Which service this API belongs. Refer to resource `tencentcloud_api_gateway_service`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestLimit

API QPS value. Enter a positive number to limit the API query rate per second `QPS`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestParameters

_Required_: No

_Type_: List of <a href="requestparametersdefinition.md">RequestParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseErrorCodes

_Required_: No

_Type_: List of <a href="responseerrorcodesdefinition.md">ResponseErrorCodesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### UpdateTime

Returns the <code>UpdateTime</code> value.

