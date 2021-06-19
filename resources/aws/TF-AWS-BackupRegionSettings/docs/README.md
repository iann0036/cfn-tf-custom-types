# TF::AWS::BackupRegionSettings

Provides an AWS Backup Region Settings resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::BackupRegionSettings",
    "Properties" : {
        "<a href="#resourcetypeoptinpreference" title="ResourceTypeOptInPreference">ResourceTypeOptInPreference</a>" : <i>[ <a href="resourcetypeoptinpreferencedefinition.md">ResourceTypeOptInPreferenceDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::BackupRegionSettings
Properties:
    <a href="#resourcetypeoptinpreference" title="ResourceTypeOptInPreference">ResourceTypeOptInPreference</a>: <i>
      - <a href="resourcetypeoptinpreferencedefinition.md">ResourceTypeOptInPreferenceDefinition</a></i>
</pre>

## Properties

#### ResourceTypeOptInPreference

A map of services along with the opt-in preferences for the Region.

_Required_: Yes

_Type_: List of <a href="resourcetypeoptinpreferencedefinition.md">ResourceTypeOptInPreferenceDefinition</a>

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

