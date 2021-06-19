# TF::Aviatrix::ControllerEmailExceptionNotificationConfig

The **aviatrix_controller_email_exception_notification_config** resource allows management of an Aviatrix Controller's email exception notification config. This resource is available as of provider version R2.19+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::ControllerEmailExceptionNotificationConfig",
    "Properties" : {
        "<a href="#enableemailexceptionnotification" title="EnableEmailExceptionNotification">EnableEmailExceptionNotification</a>" : <i>Boolean</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::ControllerEmailExceptionNotificationConfig
Properties:
    <a href="#enableemailexceptionnotification" title="EnableEmailExceptionNotification">EnableEmailExceptionNotification</a>: <i>Boolean</i>
</pre>

## Properties

#### EnableEmailExceptionNotification

Enable exception email notification. When set to true, exception email will be sent to "exception@aviatrix.com", when set to false, exception email will be sent to controller's admin email. Valid values: true, false. Default value: true.

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

#### Id

Returns the <code>Id</code> value.

