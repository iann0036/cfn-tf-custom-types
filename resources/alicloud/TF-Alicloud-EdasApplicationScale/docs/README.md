# TF::Alicloud::EdasApplicationScale

This operation is provided to scale out an EDAS application. Only these ecu scaled out will be scale in when run `terraform destroy`. 

-> **NOTE:** Available in 1.82.0+

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::EdasApplicationScale",
    "Properties" : {
        "<a href="#appid" title="AppId">AppId</a>" : <i>String</i>,
        "<a href="#deploygroup" title="DeployGroup">DeployGroup</a>" : <i>String</i>,
        "<a href="#ecuinfo" title="EcuInfo">EcuInfo</a>" : <i>[ String, ... ]</i>,
        "<a href="#forcestatus" title="ForceStatus">ForceStatus</a>" : <i>Boolean</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::EdasApplicationScale
Properties:
    <a href="#appid" title="AppId">AppId</a>: <i>String</i>
    <a href="#deploygroup" title="DeployGroup">DeployGroup</a>: <i>String</i>
    <a href="#ecuinfo" title="EcuInfo">EcuInfo</a>: <i>
      - String</i>
    <a href="#forcestatus" title="ForceStatus">ForceStatus</a>: <i>Boolean</i>
</pre>

## Properties

#### AppId

The ID of the application that you want to deploy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeployGroup

The ID of the instance group to which you want to add ECS instances to scale out the application.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcuInfo

The IDs of the Elastic Compute Unit (ECU) where you want to deploy the application. Type: List.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceStatus

This parameter specifies whether to forcibly remove an ECS instance where the application is deployed. It is set as true only after the ECS instance expires. In normal cases, this parameter do not need to be specified.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### EccInfo

Returns the <code>EccInfo</code> value.

#### Id

Returns the <code>Id</code> value.

