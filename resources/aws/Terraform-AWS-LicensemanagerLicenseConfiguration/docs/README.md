# Terraform::AWS::LicensemanagerLicenseConfiguration

Provides a License Manager license configuration resource.

~> **Note:** Removing the `license_count` attribute is not supported by the License Manager API - use `terraform taint aws_licensemanager_license_configuration.<id>` to recreate the resource instead.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::LicensemanagerLicenseConfiguration",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#licensecount" title="LicenseCount">LicenseCount</a>" : <i>Double</i>,
        "<a href="#licensecounthardlimit" title="LicenseCountHardLimit">LicenseCountHardLimit</a>" : <i>Boolean</i>,
        "<a href="#licensecountingtype" title="LicenseCountingType">LicenseCountingType</a>" : <i>String</i>,
        "<a href="#licenserules" title="LicenseRules">LicenseRules</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::LicensemanagerLicenseConfiguration
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#licensecount" title="LicenseCount">LicenseCount</a>: <i>Double</i>
    <a href="#licensecounthardlimit" title="LicenseCountHardLimit">LicenseCountHardLimit</a>: <i>Boolean</i>
    <a href="#licensecountingtype" title="LicenseCountingType">LicenseCountingType</a>: <i>String</i>
    <a href="#licenserules" title="LicenseRules">LicenseRules</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
</pre>

## Properties

#### Description

Description of the license configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseCount

Number of licenses managed by the license configuration.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseCountHardLimit

Sets the number of available licenses as a hard limit.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseCountingType

Dimension to use to track license inventory. Specify either `vCPU`, `Instance`, `Core` or `Socket`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseRules

Array of configured License Manager rules.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the license configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

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

