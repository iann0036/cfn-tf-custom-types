# Terraform::Alicloud::DbReadWriteSplittingConnection

Provides an RDS read write splitting connection resource to allocate an Intranet connection string for RDS instance.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::DbReadWriteSplittingConnection",
    "Properties" : {
        "<a href="#connectionprefix" title="ConnectionPrefix">ConnectionPrefix</a>" : <i>String</i>,
        "<a href="#distributiontype" title="DistributionType">DistributionType</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#maxdelaytime" title="MaxDelayTime">MaxDelayTime</a>" : <i>Double</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#weight" title="Weight">Weight</a>" : <i>[ <a href="weight.md">Weight</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::DbReadWriteSplittingConnection
Properties:
    <a href="#connectionprefix" title="ConnectionPrefix">ConnectionPrefix</a>: <i>String</i>
    <a href="#distributiontype" title="DistributionType">DistributionType</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#maxdelaytime" title="MaxDelayTime">MaxDelayTime</a>: <i>Double</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#weight" title="Weight">Weight</a>: <i>
      - <a href="weight.md">Weight</a></i>
</pre>

## Properties

#### ConnectionPrefix

Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <instance_id> + 'rw'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributionType

Read weight distribution mode. Values are as follows: `Standard` indicates automatic weight distribution based on types, `Custom` indicates custom weight distribution.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

The Id of instance that can run database.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDelayTime

Delay threshold, in seconds. The value range is 0 to 7200. Default to 30. Read requests are not routed to the read-only instances with a delay greater than the threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Intranet connection port. Valid value: [3001-3999]. Default to 3306.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

Read weight distribution. Read weights increase at a step of 100 up to 10,000. Enter weights in the following format: {"Instanceid":"Weight","Instanceid":"Weight"}. This parameter must be set when distribution_type is set to Custom.

_Required_: No

_Type_: List of <a href="weight.md">Weight</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ConnectionString

Returns the <code>ConnectionString</code> value.

