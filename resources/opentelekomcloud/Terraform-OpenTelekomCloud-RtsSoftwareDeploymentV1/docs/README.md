# Terraform::OpenTelekomCloud::RtsSoftwareDeploymentV1

Provides an RTS software deployment resource.

# Example Usage

 ```hcl
 
variable "config_id" {}

variable "server_id" {}
 
resource "opentelekomcloud_rts_software_deployment_v1" "mydeployment" {
  config_id = "${var.config_id}"
  server_id = "${var.server_id}"
}
 ```

# Argument Reference

The following arguments are supported:

 * `config_id` - (Required) The id of the software configuration resource running on an instance.
 
 * `server_id` - (Required) The id of the instance.
 
 * `status` -  (Optional) The current status of deployment resources.
 
 * `action` - (Optional) The stack action that triggers this deployment resource.
 
 * `input_values` - (Optional) The input data stored in the form of a key-value pair.
 
 * `output_values` - (Optional) The output data stored in the form of a key-value pair.
 
 * `status_reason` - (Optional) The cause of the current deployment resource status.
 
 * `tenant_id` - (Optional) The id of the authenticated tenant who can perform operations on the deployment resources.

# Attributes Reference

In addition to all arguments above, the following attributes are exported:

* `id` - The id of the software deployment.
 
# Import

Software deployment can be imported using the `deployment id`, e.g.
```
 $ terraform import opentelekomcloud_rts_software_deployment_v1 4779ab1c-7c1a-44b1-a02e-93dfc361b32d
 ```

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::RtsSoftwareDeploymentV1",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#configid" title="ConfigId">ConfigId</a>" : <i>String</i>,
        "<a href="#inputvalues" title="InputValues">InputValues</a>" : <i>[ <a href="inputvalues.md">InputValues</a>, ... ]</i>,
        "<a href="#outputvalues" title="OutputValues">OutputValues</a>" : <i>[ <a href="outputvalues.md">OutputValues</a>, ... ]</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#serverid" title="ServerId">ServerId</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#statusreason" title="StatusReason">StatusReason</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::RtsSoftwareDeploymentV1
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#configid" title="ConfigId">ConfigId</a>: <i>String</i>
    <a href="#inputvalues" title="InputValues">InputValues</a>: <i>
      - <a href="inputvalues.md">InputValues</a></i>
    <a href="#outputvalues" title="OutputValues">OutputValues</a>: <i>
      - <a href="outputvalues.md">OutputValues</a></i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#serverid" title="ServerId">ServerId</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#statusreason" title="StatusReason">StatusReason</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputValues

_Required_: No

_Type_: List of <a href="inputvalues.md">InputValues</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputValues

_Required_: No

_Type_: List of <a href="outputvalues.md">OutputValues</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusReason

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

_Required_: No

_Type_: String

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

