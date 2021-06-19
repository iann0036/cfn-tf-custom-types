# TF::AWS::GuarddutyOrganizationConfiguration

Manages the GuardDuty Organization Configuration in the current AWS Region. The AWS account utilizing this resource must have been assigned as a delegated Organization administrator account, e.g. via the [`aws_guardduty_organization_admin_account` resource](/docs/providers/aws/r/guardduty_organization_admin_account.html). More information about Organizations support in GuardDuty can be found in the [GuardDuty User Guide](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html).

~> **NOTE:** This is an advanced Terraform resource. Terraform will automatically assume management of the GuardDuty Organization Configuration without import and perform no actions on removal from the Terraform configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::GuarddutyOrganizationConfiguration",
    "Properties" : {
        "<a href="#autoenable" title="AutoEnable">AutoEnable</a>" : <i>Boolean</i>,
        "<a href="#detectorid" title="DetectorId">DetectorId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::GuarddutyOrganizationConfiguration
Properties:
    <a href="#autoenable" title="AutoEnable">AutoEnable</a>: <i>Boolean</i>
    <a href="#detectorid" title="DetectorId">DetectorId</a>: <i>String</i>
</pre>

## Properties

#### AutoEnable

When this setting is enabled, all new accounts that are created in, or added to, the organization are added as a member accounts of the organization’s GuardDuty delegated administrator and GuardDuty is enabled in that AWS Region.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DetectorId

The detector ID of the GuardDuty account.

_Required_: Yes

_Type_: String

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

